## 1. Project scaffolding

- [ ] 1.1 Initialize application project structure (package manager, entry point, test runner)
- [ ] 1.2 Configure environment and development scripts (start, test, migrate)
- [ ] 1.3 Add auth stub middleware that injects a fixed authenticated user context for development and tests

## 2. Persistence layer

- [ ] 2.1 Create minimal `users` seed or table to satisfy ownership precondition
- [ ] 2.2 Create `vehicles` schema with columns: id, user_id, plate, brand, model, color, created_at
- [ ] 2.3 Add UNIQUE constraint on normalized `plate` column
- [ ] 2.4 Implement `VehicleRepository` with `save(vehicle)` and `existsByPlate(normalizedPlate)` methods

## 3. Domain and validation

- [ ] 3.1 Implement `PlateNormalizer` (trim, uppercase, remove internal whitespace)
- [ ] 3.2 Implement field validator for required plate, brand, model, color (non-empty after trim, max 100 chars)
- [ ] 3.3 Define domain types/errors: `ValidationError`, `DuplicatePlateError`, `AuthenticationRequiredError`

## 4. Application service

- [ ] 4.1 Implement `VehicleRegistrationService.register(userId, input)` orchestrating normalize → validate → uniqueness check → persist
- [ ] 4.2 Ensure vehicle is always associated with the authenticated `userId` from context (never from request body)
- [ ] 4.3 Return structured success payload with registered vehicle data

## 5. HTTP API

- [ ] 5.1 Implement `POST /vehicles` endpoint wired to `VehicleRegistrationService`
- [ ] 5.2 Map success to HTTP 201 with message and vehicle object
- [ ] 5.3 Map validation errors to HTTP 400 with field-level `errors` array
- [ ] 5.4 Map duplicate plate to HTTP 409 with message "La patente ya está registrada"
- [ ] 5.5 Map missing authentication to HTTP 401

## 6. Tests

- [ ] 6.1 Test successful registration (happy path)
- [ ] 6.2 Test duplicate plate (exact and normalized variants)
- [ ] 6.3 Test each required field missing or whitespace-only
- [ ] 6.4 Test unauthenticated request returns 401
- [ ] 6.5 Test vehicle is linked to the authenticated user

## 7. Verification

- [ ] 7.1 Run full test suite and confirm all spec scenarios pass
- [ ] 7.2 Manually verify registration via API (curl or HTTP client) with auth stub
- [ ] 7.3 Update exercise status in `docs/exercises/001-register-vehicle/exercise.md` when implementation is complete
