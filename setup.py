from distutils.core import setup

setup(
    name='enjarify',
    version='1.0.4',
    description='Tool for translating Dalvik bytecode to equivalent Java bytecode',
    url='https://github.com/neskk/enjarify',
    packages=['enjarify', 'enjarify.jvm', 'enjarify.jvm.constants', 'enjarify.jvm.optimization', 'enjarify.typeinference'],
)
