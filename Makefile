.PHONY: setup clean train-lstm train-ntm experiments help

# Setup target: Create outputs directory with correct permissions
setup:
	@echo "Setting up the outputs directory..."
	mkdir -p outputs
	@echo "Setting up the models directory..."
	mkdir -p models
	@echo "Creating .env file for compose..."
	echo "HOST_UID=$(shell id -u)" > .env
	echo "HOST_GID=$(shell id -g)" >> .env
	echo "USERNAME=$(shell id -nu)" >> .env
	@echo "Setup complete."

# Start train-lstm service
train-lstm: setup
	@echo "Starting main.py in train mode with LSTM config."
	docker-compose --env-file .env up --build train-lstm
	@echo "Process completed."

# Start train-ntm service
train-ntm: setup
	@echo "Starting main.py in train mode with NTM config."
	docker-compose --env-file .env up --build train-ntm
	@echo "Process completed."

# Start experiments service
experiments: setup
	@echo "Starting main.py in experiment mode."
	docker-compose --env-file .env up --build experiments
	@echo "Process completed."

# Clean target: Stop all services and remove outputs directory
clean:
	@echo "Stopping all Docker services and cleaning up..."
	@docker-compose down -v
	@echo "Removing non-essential outputs..."
	@rm -rf outputs
	@rm -f .env
	@echo "Clean complete."

rebuild: clean setup
	@echo "Starting fresh rebuild..."
	docker-compose --env-file .env build --no-cache
	@echo "Process completed."

# Help target: List available make commands
help:
	@echo "Available targets:"
	@echo "  make train-lstm    - Setup and start the train-lstm service"
	@echo "  make train-ntm     - Setup and start the train-ntm service"
	@echo "  make experiments    - Setup and start the experiments service"
	@echo "  make clean         - Stop all services and clean up outputs directory"
	@echo "  make help          - Display this help message"
