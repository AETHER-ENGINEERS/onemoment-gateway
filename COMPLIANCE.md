# COMPLIANCE.md — TOS-Compliant AI Gateway

This gateway is designed to operate within Discord’s Terms of Service.

## Safety Rules (Non-Negotiable)

- **Only official bot token** from Developer Portal  
- **Permissions:** Send Messages, Read Message History, Use Application Commands (public channels only)  
- **Never use user tokens** or automate accounts  
- **Public channels only** — no DM/hidden channel automation  
- **Stop and report** if anything risks TOS violation  

## Architecture

- **Bot type:** Application Command (slash) only  
- **Permissions:** Minimal — no administrative rights  
- **Data retention:** No logging, no storage of user data  
- **Token management:** Environment variable only (`DISCORD_BOT_TOKEN`)

## Compliance Checklist

- [ ] Bot registered in Developer Portal  
- [ ] `DISCORD_BOT_TOKEN` stored in `.env`, never committed  
- [ ] Permissions: `Send Messages`, `Read Message History`, `Use Application Commands`  
- [ ] Only public channels active  
- [ ] No automated DMs  
- [ ] No user scraping or tracking  

---

*This gateway manifests AI helpers—never to replace humans, only to augment safe, consensual participation.*
