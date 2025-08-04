
# IMA service:

A tenant-aware identity and access management microservice, built with FastAPI. Handles user authentication, role-based authorization (RBAC), multi-organization support, and secure token-based access for accounting platform.


# ✅ Identity & Access Management (IAM) – Developer Checklist
> Goal: Securely manage users, roles, authentication, and multi-tenant access for EcoLens

---

## 🔐 1. Design & Setup
- [ ] Define data models: `User`, `Tenant`, `Organization`, `Role`, `Permission`, `Membership`
- [ ] Set up database migrations with Alembic
- [ ] Structure the FastAPI microservice: `routes`, `schemas`, `services`, `models`, `dependencies`

---

## 🔑 2. Authentication
- [ ] Implement user registration and login with email/password
- [ ] Use JWT for stateless authentication (access + refresh tokens)
- [ ] Enable secure password hashing with bcrypt
- [ ] Build token refresh endpoint
- [ ] Add forgot/reset password flow with signed email token

---

## 🧑‍🤝‍🧑 3. Multi-Tenancy & User Context
- [ ] Create tenant-aware user model (user can belong to multiple organizations)
- [ ] Implement tenant resolution from subdomain/header
- [ ] Build user role assignment logic (admin, manager, viewer, etc.)

---

## 🔐 4. Authorization (RBAC)
- [ ] Define permission levels for each role
- [ ] Create reusable role-check decorators/middleware (e.g., `@admin_required`)
- [ ] Guard sensitive endpoints with RBAC logic

---

## 🔎 5. User Session & Audit Logs
- [ ] Track login history with IP and timestamp
- [ ] Log sensitive actions like role changes, user disablement, org deletion

---

## 🌐 6. OAuth & External Identity (Optional Phase 2)
- [ ] Integrate OAuth (e.g., Google, Azure AD)
- [ ] Map external roles/groups to internal roles

---

## 🧪 7. Testing & Validation
- [ ] Write unit tests for all auth flows (signup, login, refresh, reset)
- [ ] Write authorization tests to block unauthorized access
- [ ] Write integration tests for tenant data isolation

---

## 🚀 8. DevOps & Deployment
- [ ] Create Dockerfile with health check
- [ ] Set up Azure DevOps CI/CD: lint, test, build, deploy
- [ ] Configure secure secrets management (JWT secret, SMTP, etc.)

---

## 🎯 Bonus Features (Optional)
- [ ] Implement magic link (passwordless) login
- [ ] Add rate limiting and brute-force protection
- [ ] Add session termination / device management


Project Structure:

iam/
├── app/
│   ├── api/                # Route handlers
│   │   └── v1/
│   ├── core/               # JWT, config, security
│   ├── crud/               # DB operations
│   ├── db/                 # Models & session
│   ├── schemas/            # Pydantic models
│   ├── services/           # Business logic
│   └── main.py             # FastAPI entrypoint
├── alembic/                # DB migrations
├── Dockerfile
├── requirements.txt
└── .env
