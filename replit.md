# Seashell Rarity Predictor

## Overview

This is a full-stack web application that predicts the rarity of seashells based on physical characteristics (length, width, thickness, weight, pattern, and location). Users input seashell measurements through a scientific-themed form, and the server returns a rarity classification (Common, Uncommon, Rare, or Very Rare). Prediction history is stored in a PostgreSQL database and displayed in a table.

The project also contains legacy Python scripts (`train_cnn.py`, `image_predictor.py`, `seashell_predictor.py`) for CNN-based image classification and sklearn-based prediction, but the primary application is the TypeScript web app.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend (React + Vite)
- **Location**: `client/` directory
- **Framework**: React with TypeScript, bundled by Vite
- **Routing**: `wouter` for client-side routing (single page: Home)
- **State Management**: `@tanstack/react-query` for server state (fetching predictions, history)
- **Forms**: `react-hook-form` with `@hookform/resolvers` and Zod validation
- **UI Components**: shadcn/ui (New York style) built on Radix UI primitives, styled with Tailwind CSS
- **Animations**: `framer-motion` for result transitions and loading states
- **Design Theme**: Ocean-themed scientific aesthetic with deep teals, cyans, and clean whites. Typography uses Space Grotesk (headers), Inter (body), and JetBrains Mono (data/monospace)
- **Custom Components**: `ScientificInput`, `ScientificSelect`, `RarityCard`, `HistoryList` — domain-specific components wrapping base UI primitives
- **Path Aliases**: `@/` maps to `client/src/`, `@shared/` maps to `shared/`

### Backend (Express + Node.js)
- **Location**: `server/` directory
- **Framework**: Express 5 running on Node.js with TypeScript (via `tsx`)
- **Entry Point**: `server/index.ts` creates HTTP server, registers routes, serves static files
- **API Routes** (defined in `server/routes.ts`):
  - `POST /api/predict` — accepts seashell measurements, returns rarity prediction with confidence score
  - `GET /api/history` — returns the 10 most recent predictions
- **Prediction Logic**: Server-side heuristic scoring system that simulates a Random Forest classifier. It scores based on location (Deep Sea = rarer), pattern type, shell density, and size thresholds. This is a demo approximation, not a real ML model.
- **Development**: Vite dev server is integrated as middleware for HMR during development (`server/vite.ts`)
- **Production**: Client is built to `dist/public/`, server is bundled with esbuild to `dist/index.cjs`

### Shared Code
- **Location**: `shared/` directory
- **Schema** (`shared/schema.ts`): Drizzle ORM table definitions and Zod validation schemas shared between client and server
- **Routes** (`shared/routes.ts`): API contract definitions with paths, methods, input schemas, and response types — used by both frontend hooks and backend handlers

### Database
- **ORM**: Drizzle ORM with PostgreSQL dialect
- **Connection**: `pg` Pool using `DATABASE_URL` environment variable
- **Schema**: Single table `seashell_predictions` with columns: `id` (serial PK), `length`, `width`, `thickness`, `weight` (all real), `pattern` (integer 1-4), `location` (integer 1-2), `predicted_rarity` (text)
- **Migrations**: Managed via `drizzle-kit push` (`npm run db:push`)
- **Storage Layer**: `server/storage.ts` provides a `DatabaseStorage` class implementing `IStorage` interface with `createPrediction()` and `getHistory()` methods

### Build System
- **Dev**: `npm run dev` — runs tsx with Vite middleware for HMR
- **Build**: `npm run build` — runs `script/build.ts` which builds client with Vite and server with esbuild
- **Type Check**: `npm run check` — runs TypeScript compiler
- **DB Push**: `npm run db:push` — pushes Drizzle schema to database

## External Dependencies

### Database
- **PostgreSQL** — required, connected via `DATABASE_URL` environment variable. Must be provisioned before the app runs.

### Key NPM Packages
- **drizzle-orm** + **drizzle-kit** — ORM and migration tooling for PostgreSQL
- **express** (v5) — HTTP server framework
- **@tanstack/react-query** — async server state management on the client
- **react-hook-form** + **zod** — form handling and schema validation (shared between client/server)
- **framer-motion** — animation library for UI transitions
- **shadcn/ui ecosystem** — Radix UI primitives, Tailwind CSS, class-variance-authority, clsx, tailwind-merge
- **wouter** — lightweight client-side router
- **pg** — PostgreSQL client for Node.js

### Fonts (External CDN)
- Google Fonts: Space Grotesk, Inter, JetBrains Mono, DM Sans, Fira Code, Geist Mono

### Python Dependencies (Legacy Scripts)
- TensorFlow, Pillow, NumPy, pandas, scikit-learn, tkinter — used only by standalone Python scripts, not part of the main web application