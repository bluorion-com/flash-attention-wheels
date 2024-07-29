# load("@aspect_rules_py//py:defs.bzl", "py_binary")

# filegroup(
#     name = "data",
#     srcs = glob([
#         "flash-attention-wheels/*",
#     ]),
# )

# py_binary(
#     name="setup",
#     srcs=[
#         "flash-attention-wheels/setup.py",
#     ],
#     # data = [":data"],
#     visibility=[
#         "//visibility:public",
#     ],
#     deps=[
#         "@pypi//packaging:pkg",
#         "@pypi//setuptools:pkg",
#         "@pypi//torch:pkg",
#         "@pypi//wheel:pkg",
#     ],
# )
