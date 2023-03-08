from dummy import func

def handler(context, event):
  val = dummy.func()
  return "Hello World!!!"
