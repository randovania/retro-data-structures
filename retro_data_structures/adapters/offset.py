from construct import Adapter, AdaptationError


class OffsetAdapter(Adapter):
    # stores offsets as indices

    def _get_table(self, context):
        raise NotImplementedError()

    def _get_table_length(self, context):
        raise NotImplementedError()

    def _get_base_offset(self, context):
        return 0

    def _get_item_size(self, item):
        return item.size

    def _decode(self, obj, context, path):
        table = self._get_table(context)
        offset = obj
        size = self._get_base_offset(context)

        for i in range(self._get_table_length(context)):
            if size == offset:
                return i
            if size > offset:
                raise AdaptationError("No string begins at the requested offset!")

            item = table[i]
            size += self._get_item_size(item)

    def _encode(self, obj, context, path):
        table = self._get_table(context)
        index = obj
        size = self._get_base_offset(context)

        for i in range(self._get_table_length(context)):
            if i == index:
                return size

            item = table[i]
            size += self._get_item_size(item)
