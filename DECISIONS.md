# HalalPin Strategic Decisions Log

## Architecture Decisions

### AD-001: Django Backend (Nov 12, 2025)
**Decision**: Use Django 5.0 + DRF over Laravel/Frappe/Firebase
**Rationale**: 
- 69K requests/sec performance
- Existing Python expertise
- Better for complex business logic (matching algorithms, verification)
- Cost-efficient at scale (₹10-15K/month vs Firebase ₹50K+)
**Status**: ✅ Confirmed

### AD-002: Single City Launch (Nov 12, 2025)
**Decision**: Hyderabad ONLY for first 6 months
**Rationale**:
- 40% Muslim population (highest in metros)
- Solve cold-start problem with density
- Proven marketplace strategy (Airbnb, Uber, DoorDash)
- Solo founder constraint
**Status**: ✅ Confirmed

### AD-003: Pre-Population Strategy (Nov 12, 2025)
**Decision**: Scrape/aggregate 1,000-1,500 businesses before launch
**Rationale**:
- Yelp's proven model
- Immediate user value on day 1
- Vendor FOMO (claim existing listings)
- Time saving: 40 hours vs 450 hours manual onboarding
**Status**: ✅ Confirmed

### AD-004: Separate Repositories (Nov 13, 2025)
**Decision**: halalpin-backend, halalpin-mobile, halalpin-web as separate repos
**Rationale**:
- Different deployment cycles
- Better for GitHub Copilot (focused context)
- Independent versioning
- Easier scaling with specialized teams later
**Status**: ✅ Confirmed

### AD-005: MVP Scope - Discovery Only (Nov 12, 2025)
**Decision**: Launch with discovery/listings ONLY. Exclude matrimony, travel, events, scholar council
**Rationale**:
- Focus on core value proposition
- Faster time to market (12 weeks vs 24+ weeks)
- Validate demand before building complex features
**Status**: ✅ Confirmed

## Business Model Decisions

### BD-001: Freemium Vendor Model (Nov 12, 2025)
**Decision**: Free claim + ₹999/month premium tier
**Pricing**:
- Free: Update info, 5 photos, respond to reviews, basic analytics
- Premium: Unlimited photos, enhanced placement, advanced analytics, lead capture
**Status**: ✅ Confirmed

### BD-002: Commission Structure (Nov 12, 2025)
**Decision**: Phase 2 - Optional 12% commission on bookings
**Status**: 🔄 Future consideration

## Technical Decisions

### TD-001: PostgreSQL + PostGIS (Nov 12, 2025)
**Decision**: PostgreSQL with PostGIS extension for geospatial queries
**Rationale**: Required for "halal restaurants near me" functionality
**Status**: ✅ Confirmed

### TD-002: Thread Management Strategy (Nov 13, 2025)
**Decision**: Module-by-module threading with 150K token threshold
**Rationale**:
- Natural context boundaries
- Can reference all threads in space
- Easier debugging of specific phases
**Status**: ✅ Confirmed

Last Updated: Nov 13, 2025