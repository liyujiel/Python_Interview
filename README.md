# Python_Interview

This Git Repo is for Intermediate Python developer interview.


Read List:

* [GC security problem](https://zhuanlan.zhihu.com/p/37665784?utm_source=wechat_session&utm_medium=social&utm_oi=38983023198208&from=singlemessage&isappinstalled=0&wechatShare=1) 

* [Understand threading](https://www.cnblogs.com/chengd/articles/7770898.html)

## threading Vs. thread

python提供了多种模块用来支持多线程编程，

thread（在python3中改名为_thread）,threading,和 queue模块。

通过加入queue模块，用户可以创建多个线程共享数据的队列数据结构。

thread和threading模块都可以用来创建和管理线程，而thread模块提供了基本的线程和锁支持。

threading提供的是更高级的完全的线程管理。

低级别的thread模块是推荐给高手用，一般应用程序推荐使用更高级的threading模块：

1.它更先进，有完善的线程管理支持，此外，在thread模块的一些属性会和threading模块的这些属性冲突。

2.thread模块有很少的（实际上是一个）同步原语，而threading却有很多。

3.thread模块没有很好的控制，特别当你的进程退出时，

比如：当主线程执行完退出时，其他的线程都会无警告，无保存的死亡，

而threading会允许默认，重要的子线程完成后再退出，它可以特别指定daemon类型的线程。