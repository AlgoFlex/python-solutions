class HashMap:
    def __init__(self, size=10):
        self._size = size
        self._array = [None for _ in range(size)]

    def __len__(self):
        return self._size

    def assign(self, key, value):
        index = self.__compute_index(key)
        current_value = self._array[index]

        self.__assign_value(current_value, index, key, value)
        self.__handle_assign_collision(current_value, key, value)

    def retrieve(self, key):
        index = self.__compute_index(key)
        current_value = self._array[index]

        if current_value is None:
            return None

        if current_value[0] == key:
            return self._array[index][1]

        num_of_collisions = 1
        while current_value and current_value[0] != key:
            new_index = self.__compute_index(key, num_of_collisions)
            current_value = self._array[new_index]

            if current_value is None:
                return None

            if current_value[0] == key:
                return self._array[new_index][1]

            num_of_collisions += 1

        return

    def __assign_value(self, current_value, index, key, value):
        if current_value is None:
            self._array[index] = [key, value]
            return

        if current_value[0] == key:
            self._array[index][1] = value
            return

    def __handle_assign_collision(self, current_value, key, value):
        num_of_collisions = 1
        while current_value and current_value[0] != key:
            new_index = self.__compute_index(key, num_of_collisions)
            current_value = self._array[new_index]

            self.__assign_value(current_value, new_index, key, value)
            num_of_collisions += 1

        return

    def __generate_hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def __compress(self, hash_code):
        return hash_code % self._size

    def __compute_index(self, key, count_collisions=0):
        return self.__compress(self.__generate_hash(key, count_collisions))
