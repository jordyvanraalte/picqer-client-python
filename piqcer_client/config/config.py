class Config:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Config, cls).__new__(cls)
            cls.instance.api_key = ""
            cls.instance.base_url = ""
        return cls.instance
