# HalalPin API Contract

**Version**: 1.0-MVP
**Base URL**: `https://api.halalpin.in/v1/`
**Authentication**: JWT Bearer Token

## Core Endpoints (MVP)

### Authentication
```
POST /auth/register          - User registration
POST /auth/login             - User login
POST /auth/refresh           - Refresh JWT token
POST /auth/logout            - Logout
POST /auth/verify-otp        - OTP verification
```

### Listings
```
GET  /listings                - Search listings (with filters)
GET  /listings/{id}           - Get listing details
POST /listings                - Create listing (admin/vendor)
PUT  /listings/{id}           - Update listing (owner only)
GET  /listings/near-me        - Geospatial search
```

**Query Parameters**:
- `lat`, `lng`, `radius` - Geolocation filters
- `category` - Filter by category ID
- `halal_badge` - Filter by badge tier
- `rating_min` - Minimum rating
- `search` - Text search
- `page`, `per_page` - Pagination

### Reviews
```
GET  /reviews                 - List reviews (filtered by listing)
POST /reviews                 - Create review
PUT  /reviews/{id}            - Update review (owner only)
DELETE /reviews/{id}          - Delete review (owner/admin)
POST /reviews/{id}/vendor-response - Vendor response
```

### Vendors
```
POST /vendors/claim           - Claim listing
GET  /vendors/me              - Get vendor profile
PUT  /vendors/me              - Update vendor profile
GET  /vendors/me/analytics    - Get vendor analytics
POST /vendors/me/upgrade      - Upgrade to premium
```

### Categories & Locations
```
GET  /categories              - List all categories
GET  /cities                  - List supported cities
```

## Response Format

### Success Response
```json
{
  "status": "success",
  "data": { },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 150
  }
}
```

### Error Response
```json
{
  "status": "error",
  "message": "Error description",
  "errors": {
    "field_name": ["Validation error message"]
  }
}
```

## Data Models

### Listing Object
```json
{
  "id": "uuid",
  "name": "string",
  "address": "string",
  "latitude": "float",
  "longitude": "float",
  "phone": "string",
  "category": {"id": "uuid", "name": "string"},
  "halal_badge": "certified|muslim_owned|friendly",
  "is_claimed": "boolean",
  "rating_avg": "float",
  "review_count": "integer",
  "photos": ["url1", "url2"],
  "hours": {"monday": "09:00-22:00", ...},
  "distance_km": "float"
}
```

### Review Object
```json
{
  "id": "uuid",
  "listing_id": "uuid",
  "user": {"name": "string", "avatar": "url"},
  "rating": "integer (1-5)",
  "comment": "string",
  "photos": ["url1", "url2"],
  "vendor_response": "string|null",
  "created_at": "ISO 8601 datetime"
}
```

## Mobile Clients
- Flutter app will consume this API
- React web dashboard (vendor portal) will consume this API

Last Updated: Nov 13, 2025