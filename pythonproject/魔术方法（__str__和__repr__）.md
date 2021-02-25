# 魔术方法（\_\_str\_\_和\_\_repr\_\_）



<iframe src="//player.bilibili.com/player.html?aid=370096350&bvid=BV1rZ4y1j7pu&cid=169678688&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>



- \_\_str\_\_

  1. 触发时机：使用 `print` 打印对象的时候自动触发
  2. 作用：可以定义打印对象显示的信息内容
  3. 参数：一个 `self` 接受当前对象
  4. 返回值：必须有，且必须是字符串类型
  5. 注意事项：除了 `print` 之外，使用 `str()` 转换数据的时候也会触发



- \_\_repr\_\_

  1. 触发时机：在使用 `repr` 转换对象的时候自动触发
  2. 作用：可以设置 `repr` 函数操作对象的结果
  3. 参数：一个 `self` 接受当前对象
  4. 返回值：必须有，且必须是字符串类型
  5. 注意事项：正常情况下，类中的 `__str__` 和 `__repr__` 魔术方法是完全一样的。（字符串中的`str`和`repr`魔术方法就不一样）