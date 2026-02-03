# Connect AI Documentation

This repository contains the contents of the Connect AI documentation. The documentation is powered by [Mintlify](https://www.mintlify.com). 

The Connect AI documentation is organized as follows:

- The English documentation is in the `en` directory, while the Japanese documentation is in the `ja` directory.
- I added the subfolders `API`, `Data-Sources`, `Clients`, and `SQL-Reference`. I may add more in the future.
- The `en` directory and `ja` directory each contain a `style.css` file that contains adjustments from the default Mintlify template. Any style changes go here. You need a `style.css` for each language. They are the same.
- The `en` and `ja` directories each contain an `images` directory. The images are `png` files.
- All Data Source files (in the `Data-Sources` subdirectory for each language) have a `Connect AI` and an `Embedded` version. This was necessary for the top-level navigation to work correctly. The Data Source files (Connect AI and Embedded versions) consist of a link to the same corresponding `Snippets` file. If a Data Source needs to be updated, it should be updated in the Snippets file. More on snippets below. 
- The Connect AI Integration files (in the `Clients` subdirectory for each language) contain `-Client` at the end. The Embedded versions of Integration files are named with `-Client-Embedded` at the end. They need to be updated separately, as they require different authentication. This affects some AI integrations, Dev Tools, and ETL integrations.
- The `API` directory for each language contains the API files, including API intro sections and all the endpoints. `REST-API.yaml` and `REST-API-Embedded.yaml` contain all the information needed for the API Playground part of the docs. It includes endpoint descriptions, parameter descriptions, sample output, and auth header information. The other files point to the relevant sections of the yaml files. For example, Primary-Keys.mdx points to the Primary Keys section of REST-API.yaml, and Primary-Keys-Embedded.mdx points to the Primary Keys section of REST-API-Embedded.yaml.
- The `logo` directory contains the light and dark mode versions of the CData logo.
- The `snippets` directory contains reusable snippets for the documentation. The `en` and `ja` directories each contain a `snippets` directory. There is a `Data-Sources` subdirectory for each language. This contains the data source snippets that are referenced by the Connect AI and Embedded docs. There are other snippets for text that is repeated.
- The `docs.json` file contains the global settings and the entire table of contents for the documentation website, including English and Japanese versions. More info [here](https://www.mintlify.com/docs/organize/settings). Use GitHub Copilot or another AI tool to modify this file, as it is hard to manage.
- `favicon.ico` is the favicon for the docs.
