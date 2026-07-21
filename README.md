## Known Issues

This project is a demonstration (MVP) created for TechVision and has several known limitations.

### Weather

- Weather information may occasionally display **"Unknown"** or fail to load on the first request.
- Refreshing the route or trying again usually resolves the issue.
- This happens because the weather API may temporarily fail or respond slowly.

### Geocoding

- Some place names may not be recognized if they are unavailable in the geocoding service.
- Using more specific names (e.g. city + location) improves accuracy.

### AI Recommendation

- AI recommendations depend on the availability of the Groq API.
- If the API is unavailable or the rate limit is exceeded, a default recommendation is displayed.

### Route Availability

- Route generation relies on the GraphHopper API.
- Some transportation profiles may not be available in certain regions.

### Performance

- The first request after deployment on Render may take several seconds because the free instance enters sleep mode after inactivity.

### Browser Compatibility

- The application is optimized for modern Chromium-based browsers, Firefox, and Safari.
- Older browsers may not fully support all JavaScript features.
