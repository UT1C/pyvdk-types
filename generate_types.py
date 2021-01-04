from codegen import Generator


gen = Generator(r"codegen\vk-api-schema\objects.json")
gen.write_file(r"pyvdk-types\objects.py")
