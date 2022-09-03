from pythonforandroid.recipe import PythonRecipe

class PythonBinanceRecipe(PythonRecipe):
    version = 'master'
    url = 'https://github.com/sammchardy/python-binance/archive/refs/heads/{version}.zip'

    depends = ['aiohttp', 'dateparser', 'requests', 'six', 'websockets', 'ujson']

    site_packages_name = 'python-binance'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

recipe = PythonBinanceRecipe()
