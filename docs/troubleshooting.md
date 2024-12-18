# Troubleshooting

Encountering an error, mystery, or other unexplained oddity? Open a ticket on the GitHub repository: <https://github.com/monarch-initiative/ontogpt/issues>

## I get an error like `TypeError: ConfiguredBaseModel.__init_subclass__() takes no keyword arguments`

This can happen if you have installed a version of the Pydantic package older than version 2 and/or if you're using a schema generated for Pydantic v1. Versions of OntoGPT of v0.3.3 and above should prevent this from happening, but if you're still seeing the error, then running `make` again may fix it.

## I get an error like `urllib.error.HTTPError: HTTP Error 404: Not Found`

There are a variety of reasons why this may happen, but one cause is if your schema specifies an annotator which does not exist. If the stack trace of the error includes the `get_adapter` method from `oaklib`, then this is a likely cause, and you may want to verify that all annotators are accessible to OAK.

## I get a lot of warnings like `WARNING:root:Could not find any mappings for ...` and I don't get the expected identifiers in my extracted object

Verify that the `id_prefixes` you specify in your schema correspond to those provided by the annotator. If your annotator is `sqlite:obo:hp`, for example, the prefix will be `HP` rather than `HPO`.

## I need to store the annotator files OntoGPT downloads somewhere other than `~/.data/oaklib`

OntoGPT uses `oaklib` to handle the ontologies it uses as annotators, and `oaklib` uses the `pystow` package to determine where downloads should go.

To change the download location, set the `PYSTOW_HOME` variable in your environment to your preferred path.

For example, to save downloads to `/tmp/oaklib`, set the variable like this:

```bash
export PYSTOW_HOME='/tmp/'
```

You may then reset that variable with this command:

```bash
unset PYSTOW_HOME
```

Or make the change more permanent by adding it to your `.bashrc` file and then run

```bash
source ~/.bashrc
```
