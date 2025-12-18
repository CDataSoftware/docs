# Connect AI Documentation

This repository contains the contents of the Connect AI documentation. The documentation is powered by [Mintlify](https://www.mintlify.com). 

The Connect AI documentation is organized as follows:

- The English documentation is in the `en` directory, while the Japanese documentation is in the `ja` directory.
- There are no subfolders for the documentation areas (Getting Started, Data Sources, etc.) as there were in the previous documentation repo. This is how the migration was delivered, and creating subfolders would cause issues with links. This may change in the future. 
- The `en` directory and `ja` directory each contain a `style.css` file that contains adjustments from the default Mintlify template. Any style changes go here. You need a `style.css` for each language. They are the same.
- The `en` and `ja` directories each contain an `images` directory. The images are `png` files.
- All Data Source files have a `Connect AI` and an `Embedded` version. This was necessary for the top-level navigation to work correctly. The Data Source files (Connect AI and Embedded versions) consist of a link to the same corresponding `Snippets` file. If a Data Source needs to be updated, it should be updated in the Snippets file. More on snippets below. 
- The Connect AI Integration files contain `-Client` at the end. The Embedded versions of Integration files are named with `-Client-Embedded` at the end. They need to be updated separately, as they require different authentication. This affects some AI integrations and Dev Tools integrations. 
- The `logo` directory contains the light and dark mode versions of the CData logo.
- The `snippets` directory contains reusable snippets for the documentation. This folder must be at the top level in order to work correctly (Mintlify may change this in the future). This directory contains an `en` and `ja` folder. There is a `Data-Sources` subdirectory for each language. This contains the data source snippets that are referenced by the Connect AI and Embedded docs. There are other snippets for text that is repeated.
- The `docs.json` file contains the global settings and the entire table of contents for the documentation website, including English and Japanese versions. More info [here](https://www.mintlify.com/docs/organize/settings). Use Cursor or another AI tool to modify this file, as it is hard to manage.
- `favicon.ico` is the favicon for the docs.