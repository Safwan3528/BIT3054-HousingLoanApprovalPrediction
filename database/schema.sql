CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user'
);

CREATE TABLE loan_applications (
    application_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    income FLOAT NOT NULL,
    coapplicant_income FLOAT NOT NULL,
    loan_amount FLOAT NOT NULL,
    loan_term FLOAT NOT NULL,
    credit_history FLOAT NOT NULL,
    education VARCHAR(50) NOT NULL,
    married VARCHAR(10) NOT NULL,
    dependents VARCHAR(10) NOT NULL,
    property_area VARCHAR(50) NOT NULL,
    prediction VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    application_id INTEGER NOT NULL REFERENCES loan_applications(application_id),
    result VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
