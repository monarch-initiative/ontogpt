# Troubleshooting

Encountering an error, mystery, or other unexplained oddity? Open a ticket on the GitHub repository: <https://github.com/monarch-initiative/ontogpt/issues>

## I get an error like `TypeError: ConfiguredBaseModel.__init_subclass__() takes no keyword arguments`

This can happen if you have installed a version of the Pydantic package older than version 2 and/or if you're using a schema generated for Pydantic v1. Versions of OntoGPT of v0.3.3 and above should prevent this from happening, but if you're still seeing the error, then running `make` again may fix it.
