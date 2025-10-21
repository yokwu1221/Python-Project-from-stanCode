"""
File: add2.py
Name: Yok
------------------------
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur1, lst1 = l1, []
    while cur1:
        lst1.append(cur1.val)
        cur1 = cur1.next
    total1 = 0
    power1 = len(lst1)-1
    for i in range(len(lst1)-1, -1, -1):
        num1 = lst1[i]
        total1 += num1 * 10 ** power1
        power1 -= 1

    cur2, lst2 = l2, []
    while cur2:
        lst2.append(cur2.val)
        cur2 = cur2.next
    total2 = 0
    power2 = len(lst2)-1
    for i in range(len(lst2) - 1, -1, -1):
        num2 = lst2[i]
        total2 += num2 * 10 ** power2
        power2 -= 1

    total = total1 + total2
    total = str(total)
    lst = []
    for i in range(len(total)-1, -1, -1):
        num = total[i]
        lst.append(num)
    head, cur = None, None
    dummy_node = ListNode()
    cur = dummy_node
    for num in lst:
        cur.next = ListNode(int(num))
        cur = cur.next

    return dummy_node.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type" python3 add2.py test1 "')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
