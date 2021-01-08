from codegen import Generator


files = (
    "objects",
    "responses",
)

for i in files:
    gen = Generator(fr"codegen\vk-api-schema\{i}.json")
    gen.write_file(fr"pyvdk-types\{i}.py")
