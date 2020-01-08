"""
Bài tóan: 1 cuốn sách có nhiều tác giả. 
Ta ta muốn merge trên trường tác giả
:REQUIRED: mảng đã được order theo trường book_id
data = [
    { "book_id": 1, "author_id": 1},
    { "book_id": 1, "author_id": 2},
    { "book_id": 1, "author_id": 3},
    { "book_id": 2, "author_id": 1},
    { "book_id": 2, "author_id": 7},
    { "book_id": 3, "author_id": 6}
]

expected = [
    { "book_id": 1, "author_id": "1,2,3" },
    { "book_id": 2, "author_id": "1,7" },
    { "book_id": 3, "author_id": 6}
]
"""
data = [
    {"book_id": 1, "author_id": 1},
    {"book_id": 1, "author_id": 2},
    {"book_id": 1, "author_id": 3},
    {"book_id": 2, "author_id": 1},
    {"book_id": 2, "author_id": 7},
    {"book_id": 3, "author_id": 6}
]


def merge_two_number(a: int, b: int):
    """
        :params: a = 1; b = 2
        return "1,2"
    """
    return f"{a},{b}"


def merge_duplicate_list(data):
    list_result = []
    while data != []:
        list_result.append(data.pop())
        list_result[-1]["author_id"] = str(list_result[-1]["author_id"])
        while (data != []) and (data[-1]["book_id"] == list_result[-1]["book_id"]):
            list_result[-1]["author_id"] = merge_two_number(
                list_result[-1]["author_id"], data[-1].get("author_id"))
            data.pop()
    return list_result


print(merge_duplicate_list(data))