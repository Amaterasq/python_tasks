'''
В этом упражнении вы укрепите свое мастерство паж-фу.
Вы завершите работу над классом PaginationHelper,
который является служебным классом, полезным для запроса
информации о подкачке, связанной с массивом.

Класс предназначен для приема массива значений и целого числа,
указывающего, сколько элементов будет разрешено на каждой странице.
Типы значений, содержащихся в коллекции/массиве, не имеют значения.
Ниже приведены некоторые примеры использования этого класса
'''


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        # разбить входной список на чанки
        chunks = [
            collection[i:i + items_per_page]
            for i in range(0, len(collection), items_per_page)
        ]
        # составить словарь по чанкам
        self.collection_in_chunks = {
            chunk_id: chunk for chunk_id, chunk in enumerate(chunks)
        }

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return len(self.collection_in_chunks)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index in self.collection_in_chunks:
            return len(self.collection_in_chunks.get(page_index))
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(len(self.collection)):
            return item_index // self.items_per_page
        return -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))   # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative
# indexes are invalid
