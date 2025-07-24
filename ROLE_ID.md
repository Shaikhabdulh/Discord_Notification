### 🧩 What is `ROLE_ID`?

`ROLE_ID` is the **unique identifier** for a role on your Discord server. It’s used to **@mention a specific role** (like `@Team` or `@Developers`) in your bot’s message.

---

### 🔍 Why is `ROLE_ID` optional?

- If you **want the bot to @mention a role** (e.g., notify all developers), you must provide the `ROLE_ID`.
- If you **don’t want to tag anyone**, you can **leave it out** or set it to `""` in the script logic.

---

### 🛠️ How to Use It

In your `bot.py`, this ID lets you dynamically mention a role like:

```python
f"<@&{role_id}> Good evening! Time for standup 🧘"
```

> `@&{role_id}` → Tells Discord to mention a role by ID.

---

### 📝 Summary

| Field      | Description                                     | Required? |
|------------|-------------------------------------------------|-----------|
| `ROLE_ID`  | Discord role to @mention (like @DevTeam)        | Optional  |
| `THREAD_ID`| Channel/Thread where the message is sent        | Required  |
