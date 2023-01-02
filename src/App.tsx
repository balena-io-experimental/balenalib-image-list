import "./App.css";
import { Table, Flex, Box, Provider, Heading } from "rendition";
import database from "./database/repos.json";

function App() {
  const openUrl = (url: string) => {
    window.open(url);
  };

  return (
    <Provider>
      {/* eslint-disable-next-line react/jsx-pascal-case */}
      <Heading.h3 align="left" mb={1} ml={3}>
        BalenaLib Docker Images
      </Heading.h3>
      <Flex>
        <Box width={1 / 1} m={3}>
          <Table
            columns={[
              {
                title: "Image Name",
                field: "name",
                sortable: true,
                selected: true,
              },
            ]}
            data={database}
            onRowClick={function noRefCheck(prop) {
              const url = `https://hub.docker.com/r/balenalib/${prop.name}`;
              openUrl(url);
            }}
            rowKey="name"
          />
        </Box>
      </Flex>
    </Provider>
  );
}

export default App;
