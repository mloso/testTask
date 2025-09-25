<div align="center">
  Test Task
  <br />
  <br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)

</details>

---

## About

> A test task for vacancy.

## Getting Started

### Prerequisites

> linux docker git

### Installation

```shell
git clone https://github.com/mloso/testTask && cd testTask
cp .env_dist .env  # edit your environment variables (optional)
docker compose -f docker/compose/alembic.yml -f docker/compose/database.yml -f docker/compose/networks.yml --env-file .env up --build --abort-on-container-exit
docker compose -f docker/compose/app.yml -f docker/compose/database.yml -f docker/compose/networks.yml --env-file .env up --build
```

## Usage

Go to browser and open link for swagger follow previous instruction and open `http://$HOSTNAME:$PORT/docs` page (
default - http://localhost:8080/docs)