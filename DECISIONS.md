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

### AD-002: Multi-City Launch Strategy (Nov 13, 2025) - UPDATED
**Decision**: Launch Hyderabad + Lucknow (public) + Chennai (stealth beta)
**Previous consideration**: Single city (Hyderabad only)
**Rationale**: 
- **Hyderabad** (Primary): 30% Muslim population (2.1M), tech hub, stable infrastructure
- **Lucknow** (Secondary): 25-30% Muslim (800K), Tier 2 validation, North India coverage
- **Chennai** (Stealth Beta): Founder's home base, friends/family testing, zero marketing spend
- Combined: 2.9M Muslims in public markets + 439K in stealth
- Geographic diversity: Test different Muslim demographic profiles (30%, 25%, 9%)
- Risk management: If Lucknow underperforms, Hyderabad + Chennai remain strong
- Competitor defense: Even if copied, we dominate 2 cities deeply vs competitor's multi-city spread
**Concerns addressed**:
- FOMO: Covered via 2 public + 1 stealth city
- Idea theft: Execution moat (vendor density, community trust) > idea alone
- Strategic diversity: Test high-Muslim% (Hyderabad, Lucknow) vs metro-minority (Chennai)
**Status**: ✅ Confirmed (Nov 13, 2025)

### AD-003: Pre-Population Strategy (Nov 12, 2025)
**Decision**: Scrape/aggregate vendors before launch
**Targets**:
- Hyderabad: 1,000-1,200 vendors
- Lucknow: 500-600 vendors
- Chennai: 200-300 vendors (stealth, manual curation)
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

### TD-003: Multi-City Database Schema (Nov 13, 2025)
**Decision**: City-agnostic schema with city_id foreign key
**Rationale**:
- Scalable to 50+ cities without schema changes
- Single codebase for all cities
- Location-based filtering via PostGIS
**Implementation**:
```python
class Listing(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    location = models.PointField()  # PostGIS
    # ... other fields
```
**Status**: ✅ Confirmed

## Launch Timeline

### Phase 1: Foundation (Months 1-2)
- Backend API development
- Mobile app scaffolding
- Database models
- Docker setup

### Phase 2: Pre-Population (Month 3)
- Hyderabad: 1,000 vendors
- Lucknow: 500 vendors
- Chennai: 200 vendors (stealth)

### Phase 3: Public Launch (Month 4)
- **Public**: Hyderabad + Lucknow (full marketing)
- **Stealth**: Chennai (no marketing, beta testing only)

### Phase 4: Iteration (Months 4-6)
- Fix bugs from Hyderabad/Lucknow
- Use Chennai for UX testing with friends/family
- Achieve network effects in primary markets

### Phase 5: Chennai Public Launch (Month 7+)
- **Trigger**: Hyderabad 5K+ MAU, Lucknow 2.5K+ MAU
- Full Chennai marketing with proven playbook

## Rejected Alternatives

### ❌ 5-6 City Simultaneous Launch
**Rejected**: Nov 13, 2025
**Reason**: 
- 90%+ failure probability for solo founder
- Resource dilution (200 vendors/city vs 1,000 in 1 city)
- Zero network effects in any market
- Historical failures: TinyOwl (6 cities, failed), Stayzilla (multi-city, failed)
- Successful marketplaces launch single-city: Swiggy (Koramangala only), Uber (SF only), Airbnb (SF only)

### ❌ WordPress/Voxel Theme
**Rejected**: Nov 12, 2025
**Reason**: Cannot scale to super-app vision, limited AI integration, vendor lock-in

Last Updated: Nov 13, 2025