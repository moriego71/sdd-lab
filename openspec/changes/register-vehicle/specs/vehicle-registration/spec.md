## ADDED Requirements

### Requirement: Authenticated user can register a vehicle

The system SHALL allow an authenticated driver to register a vehicle by providing plate, brand, model, and color. The vehicle MUST be associated with the authenticated user who performed the registration.

#### Scenario: Successful registration

- **WHEN** an authenticated user submits plate `ABC 123`, brand `Toyota`, model `Corolla`, and color `Blanco`
- **THEN** the system persists the vehicle linked to that user
- **AND** the system returns a success response including the registered vehicle data

#### Scenario: User not authenticated

- **WHEN** a request to register a vehicle is made without an authenticated user context
- **THEN** the system rejects the request
- **AND** the system returns an authentication error

### Requirement: Required fields validation

The system SHALL require plate, brand, model, and color for every registration attempt. All fields MUST be non-empty after trimming whitespace.

#### Scenario: Missing plate

- **WHEN** an authenticated user submits a registration without a plate (null, empty, or whitespace only)
- **THEN** the system rejects the registration
- **AND** the system returns a validation error indicating that plate is required

#### Scenario: Missing brand

- **WHEN** an authenticated user submits a registration without a brand (null, empty, or whitespace only)
- **THEN** the system rejects the registration
- **AND** the system returns a validation error indicating that brand is required

#### Scenario: Missing model

- **WHEN** an authenticated user submits a registration without a model (null, empty, or whitespace only)
- **THEN** the system rejects the registration
- **AND** the system returns a validation error indicating that model is required

#### Scenario: Missing color

- **WHEN** an authenticated user submits a registration without a color (null, empty, or whitespace only)
- **THEN** the system rejects the registration
- **AND** the system returns a validation error indicating that color is required

### Requirement: Plate uniqueness

The system SHALL ensure that each plate identifies at most one vehicle across the entire system. Plate values MUST be normalized (trimmed, uppercased, internal whitespace removed) before uniqueness checks and persistence.

#### Scenario: Duplicate plate exact match

- **WHEN** an authenticated user attempts to register a plate that already exists in the system (same normalized value)
- **THEN** the system rejects the registration
- **AND** the system returns an error indicating the plate is already registered

#### Scenario: Duplicate plate after normalization

- **WHEN** a plate `ABC 123` is already registered
- **AND** another authenticated user attempts to register plate `abc123`
- **THEN** the system rejects the registration as a duplicate
- **AND** the system returns an error indicating the plate is already registered

### Requirement: Vehicle ownership

The system SHALL associate each registered vehicle with exactly one user. A vehicle MUST NOT be assignable to a different user during registration.

#### Scenario: Vehicle linked to registering user

- **WHEN** an authenticated user with id `user-1` successfully registers a vehicle
- **THEN** the persisted vehicle MUST reference `user-1` as its owner
- **AND** the vehicle MUST NOT be owned by any other user

### Requirement: Registration feedback

The system SHALL provide clear feedback for both successful registrations and validation failures.

#### Scenario: Success message

- **WHEN** a vehicle is registered successfully
- **THEN** the system returns an explicit success indication
- **AND** the response includes the registered vehicle's plate, brand, model, and color

#### Scenario: Validation error with reason

- **WHEN** a registration fails due to validation (missing field, duplicate plate, or other rule violation)
- **THEN** the system returns an error response
- **AND** the error response identifies the reason (e.g., field name and message)
