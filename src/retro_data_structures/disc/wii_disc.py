from __future__ import annotations

import enum
import typing

import construct
from Crypto.Cipher import AES

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.disc import disc_common
from retro_data_structures.disc.disc_common import DiscHeader, ShiftedInteger

if typing.TYPE_CHECKING:
    from pathlib import Path

COMMON_KEYS = [
    # Normal
    b"\xeb\xe4\x2a\x22\x5e\x85\x93\xe4\x48\xd9\xc5\x45\x73\x81\xaa\xf7",
    # Korean
    b"\x63\xb8\x2b\xb4\xf4\x61\x4e\x2e\x13\xf2\xfe\xfb\xba\x4c\x9b\x7e",
]


class PartitionKind(enum.IntEnum):
    DATA = 0
    UPDATE = 1
    CHANNEL = 2


class SigType(enum.IntEnum):
    RSA_4096 = 0x00010000
    RSA_2048 = 0x00010001
    ELIPTICAL_CURVE = 0x00010002


class KeyType(enum.IntEnum):
    RSA_4096 = 0x00000000
    RSA_2048 = 0x00000001


PartitionInfoHeader = construct.Struct(
    total_partitions=construct.Int32ub, info_offset=ShiftedInteger(construct.Int32ub)
)
PartInfo = construct.Struct(
    data_offset=ShiftedInteger(construct.Int32ub),
    kind=EnumAdapter(PartitionKind),
)

Ticket = construct.Struct(
    "sig_type" / construct.Const(SigType.RSA_2048, EnumAdapter(SigType)),
    "sig" / construct.Bytes(256),
    construct.Padding(60),
    "sig_issuer" / construct.Bytes(64),
    "ecdh" / construct.Bytes(60),
    construct.Padding(3),
    "enc_key" / construct.Bytes(16),
    construct.Padding(1),
    "ticket_id" / construct.Bytes(8),
    "console_id" / construct.Bytes(4),
    "title_id" / construct.Bytes(8),
    construct.Padding(2),
    "ticket_version" / construct.Int16ub,
    "permitted_titles_mask" / construct.Int32ub,
    "permit_mask" / construct.Int32ub,
    "title_export_allowed" / construct.Flag,
    "common_key_idx" / construct.Int8ub,
    construct.Padding(48),
    "content_access_permissions" / construct.Bytes(64),
    construct.Padding(2),
    "time_limits"
    / construct.Struct(
        enable_time_limit=construct.Int32ub,
        time_limit=construct.Int32ub,
    )[8],
)
assert Ticket.sizeof() == 0x2A4

PartitionHeader = construct.Struct(
    ticket=Ticket,
    tmd_size=construct.Int32ub,
    tmd_offset=ShiftedInteger(construct.Int32ub),
    cert_chain_size=construct.Int32ub,
    cert_chain_offset=ShiftedInteger(construct.Int32ub),
    global_hash_table_size=construct.Computed(0x18000),
    global_hash_table_offset=ShiftedInteger(construct.Int32ub),
    data_offset=ShiftedInteger(construct.Int32ub),
    data_size=construct.Int32ub,
)

TMD = construct.Struct(
    header=construct.Aligned(
        64,
        construct.Struct(
            sig_type=EnumAdapter(SigType),
            sig=construct.Bytes(256),
        ),
    ),
    sig_issuer=construct.Bytes(64),
    versions=construct.Aligned(
        4,
        construct.Struct(
            main=construct.Byte,
            ca_crl=construct.Byte,
            signer_crl=construct.Byte,
        ),
    ),
    ios_id_major=construct.Int32ub,
    ios_id_minor=construct.Int32ub,
    title_id_major=construct.Int32ub,
    title_id_minor=construct.Bytes(4),
    title_type=construct.Int32ub,
    group_id=construct.Int16ub,
    padding3=construct.Bytes(62),
    access_flags=construct.Int32ub,
    title_version=construct.Int16ub,
    _num_contents=construct.Rebuild(construct.Int16ub, construct.len_(construct.this.contents)),
    boot_idx=construct.Int16ub,
    padding4=construct.Int16ub,
    contents=construct.Array(
        construct.this._num_contents,
        construct.Struct(
            id=construct.Int32ub,
            index=construct.Int16ub,
            type=construct.Int16ub,
            size=construct.Int64ub,
            hash=construct.Bytes(20),
        ),
    ),
)

Certificate = construct.Struct(
    sig_type=EnumAdapter(SigType),
    sig=construct.Switch(
        construct.this.sig_type,
        {
            SigType.RSA_2048: construct.Bytes(256),
            SigType.RSA_4096: construct.Bytes(512),
            SigType.ELIPTICAL_CURVE: construct.Bytes(64),
        },
        construct.Error,
    ),
    _skip1=construct.Const(b"\x00" * 60),
    issuer=construct.Bytes(64),
    key_type=EnumAdapter(KeyType),
    subject=construct.Bytes(64),
    key=construct.Switch(
        construct.this.key_type,
        {
            KeyType.RSA_2048: construct.Bytes(256),
            KeyType.RSA_4096: construct.Bytes(512),
        },
        construct.Error,
    ),
    modulus=construct.Int32ub,
    pub_exp=construct.Int32ub,
    _skip2=construct.Const(b"\x00" * 52),
)

FileEntry = construct.Struct(
    is_directory=construct.Flag,
    file_name=construct.Int24ub,
    offset=ShiftedInteger(construct.Int32ub),
    param=construct.Int32ub,
)
RootFileEntry = construct.Struct(
    is_directory=construct.Const(True, construct.Flag),
    file_name=construct.Const(0, construct.Int24ub),
    _offset=construct.Const(0, construct.Int32ub),
    num_entries=construct.Int32ub,
)


class EncryptedDiscFileReader(disc_common.DiscFileReader):
    """
    Reads encrypted Wii Disc Partitions
    """

    def __init__(self, file: Path | typing.BinaryIO, size: int, dec_key: bytes, base_offset: int, offset: int):
        super().__init__(
            file,
            base_offset,
            size,
        )

        self._dec_key = dec_key
        self._initial_offset = offset
        self._offset = offset
        self._cur_block = -1
        self._dec_buf = bytearray(0x8000 - 0x400)

    def _decrypt_block(self, block: int) -> None:
        self._cur_block = block
        self._file.seek(self._base_offset + self._cur_block * 0x8000)
        enc_buf = memoryview(self._file.read(0x8000))
        aes = AES.new(key=self._dec_key, mode=AES.MODE_CBC, iv=enc_buf[0x3D0:0x3E0])
        aes.decrypt(enc_buf[0x400:], self._dec_buf)

    def read(self, size: int = -1) -> bytes:
        block_quot = self._offset // 0x7C00
        block_rem = self._offset % 0x7C00

        if size == -1:
            size = self._size - (self._offset - self._initial_offset)

        ret = bytearray()
        rem = size

        while rem > 0:
            if block_quot != self._cur_block:
                self._decrypt_block(block_quot)

            cache_size = rem
            if cache_size + block_rem > 0x7C00:
                cache_size = 0x7C00 - block_rem

            ret += memoryview(self._dec_buf)[block_rem : block_rem + cache_size]
            rem -= cache_size
            block_rem = 0
            block_quot += 1

        self._offset += size
        return ret

    def seek(self, offset: int, whence: int = 0) -> None:
        if whence == 0:
            self._offset = offset
        elif whence == 1:
            self._offset += offset
        else:
            return

    def tell(self) -> int:
        return self._offset


class WiiPartition:
    def __init__(self, source: typing.BinaryIO, part_info: construct.Container):
        self._part_info = part_info
        source.seek(part_info.data_offset)

        self._part_header = PartitionHeader.parse_stream(source)
        self._data_offset = part_info.data_offset + self._part_header.data_offset

        source.seek(part_info.data_offset + self._part_header.tmd_offset)
        self._tmd = TMD.parse_stream(source)

        source.seek(part_info.data_offset + self._part_header.cert_chain_offset)
        self._ca_cert = Certificate.parse_stream(source)
        self._tmd_cert = Certificate.parse_stream(source)
        self._ticket_cert = Certificate.parse_stream(source)

        source.seek(part_info.data_offset + self._part_header.global_hash_table_offset)
        self._h3_data = source.read(self._part_header.global_hash_table_size)

        aes = AES.new(
            key=COMMON_KEYS[self._part_header.ticket.common_key_idx],
            mode=AES.MODE_CBC,
            iv=self._part_header.ticket.title_id + b"\x00" * 8,
        )
        self._dec_key = aes.decrypt(self._part_header.ticket.enc_key)

        ds = self.begin_read_stream(source, 0, -1)
        self.disc_header = DiscHeader.parse_stream(ds)
        self.disc_header_info = disc_common.DiscHeaderInformation.parse_stream(ds)

        ds.seek(0x2440 + 0x14)
        vals = (construct.Int32ub[2]).parse_stream(ds)
        self.app_loader_sz = 32 + vals[0] + vals[1]

        ds.seek(self.disc_header.fst_offset)
        self.fst = disc_common.file_system_tree(
            self.disc_header.fst_size, ShiftedInteger(construct.Int32ub)
        ).parse_stream(ds)

    def begin_read_stream(
        self, file_io: Path | typing.BinaryIO, offset: int, file_size: int
    ) -> disc_common.DiscFileReader:
        return EncryptedDiscFileReader(file_io, file_size, self._dec_key, self._data_offset, offset)


class WiiDiscConstruct(construct.Construct):
    def _parse(self, stream: typing.BinaryIO, context: construct.Container, path: str) -> construct.Container:
        header = DiscHeader.parse_stream(stream)

        part_infos = []
        partitions = []

        stream.seek(0x40000)
        partition_info = PartitionInfoHeader.parse_stream(stream)
        stream.seek(partition_info.info_offset)

        for i in range(min(4, partition_info.total_partitions)):
            part_infos.append(PartInfo.parse_stream(stream))

        data_partition = None
        for part_info in part_infos:
            partitions.append(WiiPartition(stream, part_info))
            if part_info.kind == PartitionKind.DATA:
                data_partition = partitions[-1]

        return construct.Container(
            header=header,
            partitions=partitions,
            data_partition=data_partition,
        )


WiiDisc = WiiDiscConstruct()
