# Platzi FastAPI - Customer Management System

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-Latest-orange.svg)](https://sqlmodel.tiangolo.com/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern, fast (high-performance) web API built with FastAPI for managing customers, transactions, plans, and invoices. This project demonstrates best practices in API development using Python's latest features and modern frameworks.

## 🚀 Features

- **RESTful API** with automatic interactive documentation
- **Customer Management** - Create, read, update, and delete customer records
- **Transaction Tracking** - Handle financial transactions linked to customers
- **Subscription Plans** - Manage different service plans for customers
- **Invoice Generation** - Automatically generate invoices from transactions
- **Database Integration** - SQLModel with SQLite for data persistence
- **Type Safety** - Full type hints and Pydantic models for data validation
- **Interactive Documentation** - Automatic OpenAPI/Swagger UI

## 📋 Table of Contents

- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Database Models](#-database-models)
- [Development](#-development)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

## 🛠 Installation

### Prerequisites

- Python 3.12+
- Conda (recommended) or pip

### Using Conda (Recommended)

1. Clone the repository:

```bash
git clone https://github.com/jasonssdev/platzi-fastapi.git
cd platzi-fastapi
```

2. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate fastapi-py312
```

3. Install additional dependencies if needed:

```bash
conda install uvicorn
```

### Using pip

1. Clone the repository:

```bash
git clone https://github.com/jasonssdev/platzi-fastapi.git
cd platzi-fastapi
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi sqlmodel uvicorn
```

## 🚀 Quick Start

1. Start the development server:

```bash
uvicorn app.main:app --reload
```

2. Open your browser and navigate to:
   - **API Documentation**: <http://localhost:8000/docs>
   - **Alternative Documentation**: <http://localhost:8000/redoc>
   - **API Root**: <http://localhost:8000/>

3. Test the API:

```bash
curl http://localhost:8000/
# Response: {"message": "Hello World"}

curl http://localhost:8000/time
# Response: {"current_time": "2025-01-XX XX:XX:XX"}
```

## 📚 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/time` | Current server time |

### Customer Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/customers/` | List all customers |
| `POST` | `/customers/` | Create a new customer |
| `GET` | `/customers/{id}` | Get customer by ID |
| `PUT` | `/customers/{id}` | Update customer |
| `DELETE` | `/customers/{id}` | Delete customer |

### Transaction Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/transactions/` | List all transactions |
| `POST` | `/transactions/` | Create a new transaction |
| `GET` | `/transactions/{id}` | Get transaction by ID |

### Plan Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/plans/` | List all plans |
| `POST` | `/plans/` | Create a new plan |
| `GET` | `/plans/{id}` | Get plan by ID |

### Invoice Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/invoices/` | Create a new invoice |

## 📁 Project Structure

```text
platzi-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   └── routers/
│       ├── __init__.py
│       ├── customers.py     # Customer endpoints
│       ├── transactions.py  # Transaction endpoints
│       ├── plans.py         # Plan endpoints
│       └── invoices.py      # Invoice endpoints
├── models.py                # SQLModel database models
├── db.py                    # Database configuration
├── environment.yml          # Conda environment configuration
├── pyproject.toml          # Project configuration
├── db.sqlite3              # SQLite database file
└── README.md               # Project documentation
```

## 🗄 Database Models

The application uses SQLModel for database operations with the following models:

- **Customer**: User information with name, email, age, and description
- **Transaction**: Financial transactions linked to customers
- **Plan**: Subscription plans with pricing and descriptions
- **CustomerPlan**: Many-to-many relationship between customers and plans
- **Invoice**: Generated invoices containing customer and transaction data

### Model Relationships

```text
Customer ←→ Transaction (One-to-Many)
Customer ←→ Plan (Many-to-Many via CustomerPlan)
Invoice → Customer (One-to-One)
Invoice → Transaction (One-to-Many)
```

## 🔧 Development

### Code Style

This project follows Python best practices:

- **Type Hints**: Full type annotation coverage
- **Pydantic Models**: Data validation and serialization
- **SQLModel**: Type-safe database operations
- **Separation of Concerns**: Clean architecture with routers

### Adding New Features

1. Create new models in `models.py`
2. Add database operations in `db.py`
3. Create new router in `app/routers/`
4. Register router in `app/main.py`

### Environment Variables

The application can be configured using environment variables:

```bash
export DATABASE_URL="sqlite:///./db.sqlite3"
export DEBUG=True
```

## 🧪 Testing

To run tests (when implemented):

```bash
# Install testing dependencies
conda install pytest pytest-asyncio httpx

# Run tests
pytest
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Write docstrings for classes and functions
- Add tests for new features

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQL databases in Python with type safety
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Platzi](https://platzi.com/) - Educational platform inspiration

## 📞 Contact

Jason SS - [@jasonssdev](https://github.com/jasonssdev)

Project Link: [https://github.com/jasonssdev/platzi-fastapi](https://github.com/jasonssdev/platzi-fastapi)

---

⭐ If you find this project helpful, please give it a star on GitHub!