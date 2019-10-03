# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict
class LRUCache:
  def __init__(self, capacity: int):
    self.storage = OrderedDict()
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key in self.storage:
      # moves the key to ordered dict's end
      # if last = False, the key would be the next item removed on put
      self.storage.move_to_end(key, last=True)
      return self.storage[key]
    return -1

  def put(self, key: int, value: int) -> None:
    self.storage[key] = value
    self.storage.move_to_end(key, last=True)
    if len(self.storage) - 1 >= self.capacity:
      # last = False makes it so that the ordered dict
      # removes items in a FIFO (first in first out) order
      self.storage.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)