# balenalib image list

Generates and stores the balenalib Docker Hub image names/URLs and serves them in a web UI using [Rendition](https://github.com/balena-io-modules/rendition). The UI is deployed to GitHub Pages via this repository.

Markdown files are also generated and stored in the root directory of this repository. `repos.md` uses the default markdown approach of opening URLs, which means they open in the same tab. `repos_html.md` uses html which allows opening pages in new tabs (although GitHub doesn't support this so html defaults back to opening in the same tab).

The GitHub action runs on a schedule (see `./.github/workflows/build.yml`), updating the database and deploying a new UI to keep it up to date.

To update the database file (`src/database/repos.json`) and deploy manually trigger a run of the `build.yml` GitHub action.

To deploy the UI manually with the available database file trigger a run of the `deploy-to-github-pages.yml` GitHub action.

## Development

The Python build script for compiling the JSON file is `build.py`.

For the UI, install the dependencies with `npm ci`.

Then in the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.
