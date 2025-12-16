# Docker Workshop — Pipeline

Overview

This repository contains a small data pipeline project under the `pipeline/` directory that is built and run using Docker and Docker Compose. The intention of this repo is to provide a self-contained example of containerized ingestion and pipeline execution.

Contents

- `pipeline/docker-compose.yaml` — service orchestration used to run the pipeline with Docker Compose.
- `pipeline/Dockerfile` — image build instructions for the pipeline service.
- `pipeline/pipeline.py` — main pipeline program.
- `pipeline/ingest_data.py` — example ingestion script.
- `pipeline/pyproject.toml` — Python project metadata and dependencies.

Quick start

1. Open a terminal in the repository root:

```bash
cd pipeline
```

2. Build and run the pipeline with Docker Compose:

```bash
docker compose up --build
# or, if your environment uses the older CLI:
docker-compose up --build
```

3. Run in detached mode:

```bash
docker compose up -d --build
```

Run without Docker

If you prefer to run the pipeline locally without Docker, install the Python dependencies from `pyproject.toml` (for example via `pip install .` or `poetry install`) and run:

```bash
python pipeline/pipeline.py
```

Running the built image directly

After building the image (either via `docker compose build` or `docker build` from the `pipeline/` folder), you can run the image directly with `docker run`. The example below demonstrates how to run the `taxi_ingest:v001` image and connect it to the PostgreSQL service created by `docker-compose` (this assumes the Compose network is `pipeline_pg-network` and the Postgres service hostname is `pgdatabase`):

```bash
docker run -it --rm \
	--network=pipeline_pg-network \
	taxi_ingest:v001 \
		--pg-user=root \
		--pg-pass=root \
		--pg-host=pgdatabase \
		--pg-port=5432 \
		--pg-db=ny_taxi \
		--target-table=yellow_taxi_trips_2021_01 \
		--year=2021 \
		--month=01 \
		--chunksize=100000
```

What this image does

- The container runs the ingestion job (the image entrypoint executes `ingest_data.py`) and writes rows into the `ny_taxi` database on the `pgdatabase` Postgres service defined in `pipeline/docker-compose.yaml`.
- Confirm the service name and network in `pipeline/docker-compose.yaml` if you need to run the image manually outside of `docker compose up`.


Notes

- Check `pipeline/docker-compose.yaml` for any environment variables or service ports that you may need to configure.
- Use `docker compose logs -f` to tail logs from running services.
- Clean up resources with:

```bash
docker compose down --rmi local --volumes --remove-orphans
```

