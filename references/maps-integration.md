# RTPTPA Google Maps Platform + deck.gl Integration

## Purpose
Geo-locate the Relative-Tensor Power-Tower Prompt Arbitration (RTPTPA-QCG) system as a holographic scientific dashboard over real-world research infrastructure — specifically **NASA Ames Research Center** (Moffett Field, California), home of the Quantum Artificial Intelligence Laboratory (QuAIL).

This enables:
- Thermodynamic / Landauer entropy fields visualized as heatmaps over actual campus buildings
- Diamond NV spin-stabilization nodes as scatter points
- Power-tower hierarchical arcs (thermodynamic → quantum → control → genesis)
- Relative-tensor network overlays
- Live camera tilt / orbit for Genesis Conductor demos and public science communication

## Coordinates
- **NASA Ames Research Center**: 37.4153° N, 122.0628° W (Moffett Field)

## Architecture (official GMP recommendation)
Use **deck.gl `GoogleMapsOverlay`** on top of the Maps JavaScript API vector basemap:

- **Interleaved mode** (`interleaved: true`) preferred so WebGL layers correctly occlude with 3D campus buildings and terrain.
- Fall back to overlaid mode if vector map / WebGL2 unavailable.
- HeatmapLayer for continuous entropy / GPU thermal fields.
- ScatterplotLayer / custom layers for discrete NV centers and tensor nodes.
- ArcLayer or PathLayer for power-tower / relative-tensor connections.

### Key documentation (with attribution)
- [deck.gl + Google Maps Overlay](https://developers.google.com/maps/documentation/javascript/deckgl-overlay-view?utm_source=gmp-code-assist)
- [HeatmapLayer example](https://developers.google.com/maps/documentation/javascript/examples/deckgl-heatmap?utm_source=gmp-code-assist)
- [WebGL Overlay View](https://developers.google.com/maps/documentation/javascript/webgl/webgl-overlay-view?utm_source=gmp-code-assist)
- [Vector maps & tilt/rotation](https://developers.google.com/maps/documentation/javascript/vector-map?utm_source=gmp-code-assist)

## Live Demo
Open `examples/maps-deckgl-rtptpa.html` after inserting a restricted Maps JavaScript API key.

The HTML also includes the required internalUsageAttributionIds for Code Assist tracking.

## Imagine-generated Visualization
A 6-second cinematic video of the full RTPTPA dashboard holographically projected over the Ames satellite/hybrid map (night mode, glowing roads, QuAIL labels) was generated and is available in the conversation history as asset `2c282636-2148-41f7-a83c-1212f043e5b0`.

## Production Notes
- Restrict API keys (HTTP referrers / APIs) per Google Cloud best practices.
- Prefer cloud Map IDs for advanced styling and vector features.
- Replace synthetic data in the demo with live streams from `scripts/rtpTPA.py` (thermo_state, relative tensors, control_spec).
- For multi-site networks (other NV labs, Kovach Enterprises nodes), extend the data arrays and use clustering or multi-view.

## License & Attribution
MIT (repo). Google Maps Platform code snippets are provided under Apache 2.0 and are subject to the Google Maps Platform Terms of Service.

Principal Investigator: Igor Holt (ORCID 0009-0008-8389-1297)
