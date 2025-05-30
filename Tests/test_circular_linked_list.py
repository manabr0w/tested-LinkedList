import pytest
from CircularLinkedListClass import CircularLinkedList

def test_append():
    cll = CircularLinkedList()
    cll.append('A')
    cll.append('B')
    assert str(cll) == "['A', 'B']"
    assert cll.length() == 2

def test_insert():
    cll = CircularLinkedList()
    cll.append('A')
    cll.append('C')
    cll.insert('B', 1)
    cll.insert('X', 0)
    cll.insert('Z', cll.length())
    assert str(cll) == "['X', 'A', 'B', 'C', 'Z']"

def test_delete():
    cll = CircularLinkedList()
    for ch in 'ABCDE':
        cll.append(ch)
    deleted = cll.delete(0)
    assert deleted == 'A'
    deleted = cll.delete(2)
    assert deleted == 'D'
    deleted = cll.delete(cll.length() - 1)
    assert deleted == 'E'
    assert str(cll) == "['B', 'C']"

def test_delete_all():
    cll = CircularLinkedList()
    for ch in 'ABACADA':
        cll.append(ch)
    cll.deleteAll('A')
    assert str(cll) == "['B', 'C', 'D']"

def test_get():
    cll = CircularLinkedList()
    cll.append('X')
    cll.append('Y')
    cll.append('Z')
    assert cll.get(0) == 'X'
    assert cll.get(1) == 'Y'
    assert cll.get(2) == 'Z'

def test_find_first_last():
    cll = CircularLinkedList()
    for ch in 'ABACABA':
        cll.append(ch)
    assert cll.findFirst('A') == 0
    assert cll.findLast('A') == 6
    assert cll.findFirst('Z') == -1

def test_reverse():
    cll = CircularLinkedList()
    for ch in 'ABC':
        cll.append(ch)
    cll.reverse()
    assert str(cll) == "['C', 'B', 'A']"

def test_clone():
    cll = CircularLinkedList()
    for ch in 'XYZ':
        cll.append(ch)
    cloned = cll.clone()
    assert str(cll) == str(cloned)
    cll.delete(0)
    assert str(cll) != str(cloned)

def test_clear():
    cll = CircularLinkedList()
    for ch in '123':
        cll.append(ch)
    cll.clear()
    assert cll.length() == 0
    assert str(cll) == "[]"

def test_extend():
    list1 = CircularLinkedList()
    list2 = CircularLinkedList()
    for ch in 'ABC':
        list1.append(ch)
    for ch in 'XYZ':
        list2.append(ch)
    list1.extend(list2)
    assert str(list1) == "['A', 'B', 'C', 'X', 'Y', 'Z']"
