{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reversing a linked list\n",
    "# runtime complexity: O(N) Memory  O(1)\n",
    "#its being changed in place iteritively\n",
    "class ListNode:\n",
    "    def __init__(self, val=0, next=None):\n",
    "        self.val = val\n",
    "        self.next = next\n",
    "class Solution:\n",
    "    def reverseList(head):\n",
    "        prev = None\n",
    "        curr = head\n",
    "        while curr:\n",
    "            future = curr.next \n",
    "            curr.next = prev    #this line makes the linkedlist pointer point to the side of the list that has already been reversed!\n",
    "            prev  = curr  \n",
    "            curr = future       \n",
    "        return prev "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#reverse a linked list recursively \n",
    "#runtime complexity O(N) Memory O(1)\n",
    "class ListNode:\n",
    "    def __init__(self, val=0, next=None):\n",
    "        self.val = val\n",
    "        self.next = next\n",
    "class Solution:\n",
    "    def reverseList(head):\n",
    "        prev = None\n",
    "        head.next = prev\n",
    "        reverseList(head.next)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
