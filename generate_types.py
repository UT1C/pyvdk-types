from codegen import ObjectGenerator


files = (
    "objects",
    "responses",
)

for i in files:
    gen = ObjectGenerator(fr"codegen\vk-api-schema\{i}.json")
    gen.write_file(fr"pyvdk_types\{i}.py")
