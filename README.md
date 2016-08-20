## Coding Standards

- python 3.5.12 (Don't use python2 anywhere)
- Follow [https://www.python.org/dev/peps/pep-0008/](PEP8 style guide)
- Use 4 spaces instead of tabs.
- Use 4 spaces in HTML (it is the django specs, HTML guide says 2, but let's follow django)
- Work on branches, and merge to master once you are confident that it works.
- Use pylint (Ingore this for now).

## Prerequistes:

- node (>6.0.0) (install with [https://github.com/creationix/nvm](nvm), just install the latest version)
- webpack and grunt's cli. Install with `npm install -g webpack webpack-dev-server grunt-cli`

## Running the dev server:

in two different terminals, run: `python manage.py runserver` and `grunt watch`

## Deploying to heroku:

TODO(fyquah): Write up about this.

## Products

1. Products (physical)

- Single Product (detail view) --> Social Sharing Buttons
- List Product (list view)
- Inventory Control + Viewable
- Search Products

2. Checkout

- Cart (shopping cart)
- Auth Users & Guest User (non-auth)
- Shipping & Billing Address

3. Payment

- Integration with Braintree (steps on other integrations)
