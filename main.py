import qrcode

image = qrcode.make("Hey, tsup")
image.save("hello.png")