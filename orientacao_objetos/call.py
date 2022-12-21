class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print('Chamando, ', self.phone)


call1 = CallMe('121232')
call1()
