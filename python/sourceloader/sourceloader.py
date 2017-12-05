from importlib.machinery import SourceFileLoader

loader = SourceFileLoader('ello', 'somesource.py')
module = loader.load_module()

module.main()
