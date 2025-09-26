from __future__ import annotations

import hashlib

import pytest

from retro_data_structures.formats import Txtr

# from quicktex.s3tc.bc1 import BC1Block, BC1Texture, BC1Encoder, BC1Decoder
# decoder = BC1Decoder(write_alpha=False)
# in_texture = BC1Texture.from_bytes(t.raw.image_data, t.width, t.height)
#
# out_texture = decoder.decode(in_texture)
# assert out_texture.size == (t.width, t.height)
#
# out_img = Image.frombytes('RGBA', (t.width, t.height), out_texture.tobytes())


@pytest.mark.parametrize(
    ["asset_id", "expected_hash"],
    [
        pytest.param(0x1E23D8B7, "37bfd7f3153e30142d1db1114c4908beccfd103c5a1e8aa4bdba206d5d31d5ba", id="I4"),
        pytest.param(0xF7A4D1A6, "ae9d13c2e7a537a0d8e19024042b996f7bf5ee87e2aac145185108d3719a29da", id="I8"),
        pytest.param(0x2C9D1857, "eecc2d55d95c0fbd4ad59fc1ac216613292839d1e64837523e59472add63b9d7", id="IA4"),
        pytest.param(0x5AA3955A, "dde9392764ea131a0845a725289538ffe0b4fa11de6251d8a8b58e67932c7f3f", id="IA8"),
        pytest.param(0x72D5D9C4, "", id="C4"),
        pytest.param(0x9B6D149A, "", id="C8"),
        pytest.param(0x860048C3, "e2078fe3f250488b2813f5194f271beca506bc3b69b5978a592d59bf7209ddb5", id="RGB565"),
        pytest.param(0x1940092C, "cc5d38f7f0f2cd6381c657540ba4b0faba146d35f8f1eb973aee7409193a853b", id="RGB5A3"),
        pytest.param(0x6FC03D46, "e61d3d9cb9ab05f16e666291bb4696f1037776264d1065a12dbba7a20e0885e9", id="RGBA8"),
        pytest.param(0x0151FA12, "5910604c977424a69b7dd9b9ff19823c0314c30600fa647e71b5db939c2a5e1a", id="CMPR"),
    ],
)
def test_txtr_by_hash(prime2_asset_manager, asset_id, expected_hash):
    raw = prime2_asset_manager.get_raw_asset(asset_id)
    t = Txtr.parse(raw.data, prime2_asset_manager.target_game, prime2_asset_manager)

    data = t.main_image_data.tobytes("raw")
    assert hashlib.sha256(data).hexdigest() == expected_hash
