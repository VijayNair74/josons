# Josons Spices website — going live on Cloudflare Pages (free)

Everything runs on Cloudflare's free plan: the website, the enquiry store (D1 database) and Manu's private admin page.
Time needed: about 20 minutes.

## 1. Create the site
1. Sign up at https://dash.cloudflare.com (free).
2. Go to **Workers & Pages → Create → Pages → Upload assets**.
3. Name the project `josons`. Upload the unzipped site folder: `index.html`, `admin.html`, the `img`, `pdf` and `functions` folders, and `schema.sql`.
   - If the upload page ignores the `functions` folder, use the command line instead (step 5).

## 2. Create the enquiry database
1. **Workers & Pages → D1 → Create database**, and name it `josons`.
2. Open it, go to **Console**, paste the contents of `schema.sql`, and run it.

## 3. Connect the database to the site
In the Pages project, go to **Settings → Bindings → Add → D1 database**:
- **Variable name:** `DB`
- **Database:** `josons`

## 4. Set Manu's admin password
In the Pages project, go to **Settings → Variables and secrets → Add**:
- **Type:** Secret
- **Name:** `ADMIN_PASSWORD`
- **Value:** a long password, 12 characters or more. Give it to Manu only.

Then **redeploy**: go to **Deployments**, then **Retry deployment**, so the binding and secret take effect.

## 5. (If needed) Deploy from the command line
```
npm i -g wrangler
wrangler login
wrangler pages deploy . --project-name josons
```
Run it from inside the site folder.

## 6. Use it
- **Website:** `https://josons.pages.dev`. You can add a custom domain such as josonsspices.in under **Custom domains**.
- **Manu's CRM and enquiry desk:** `https://josons.pages.dev/admin.html` (see the CRM section below)
  - Status: New → Quoted → Sample sent → Ordered / Lost
  - A follow-up date highlights the card when it's due
  - **Reply on WhatsApp** opens a chat with the buyer
  - **Export CSV** saves a copy before clearing
  - **Clear closed > 30 days** removes old Ordered/Lost enquiries; **Delete all** wipes everything
  - Both clear buttons need two taps to confirm

## Notes
- The buyer's WhatsApp message to Manu is the real enquiry. The saved copy is for tracking only, so if saving ever fails, Manu still gets the message.
- **Privacy:** buyer names and phone numbers are personal data. Keep the password private and clear old enquiries regularly. India's DPDP Act expects data to be kept only as long as needed.
- **To change the password:** update the secret, then redeploy.

## CRM (leads, conversation log, AI assistant)

`/admin.html` is now Manu's CRM. It uses the same `DB` database and `ADMIN_PASSWORD` as before. The tables are created automatically the first time he signs in, so there is no SQL to run. The old enquiry desk is still there under the **Enquiries** tab.

**First-time steps**
1. Sign in at `/admin.html` on his phone and choose **Add to Home screen** in the browser menu.
2. **More → Import leads**: choose `josons_leads_import.csv` (the 200 prospects). Do the same for a list of past customers, with `Y` in the `is_customer` column. Companies already in the list are skipped, so re-running is safe.
3. **Turn on the AI assistant** (optional but recommended): in the Pages project, go to **Settings → Variables and secrets → Add**:
   - **Type:** Secret, **Name:** `ANTHROPIC_API_KEY`, **Value:** the API key (create it at console.anthropic.com, and set a monthly spend limit there)
   - Optional plain variables: `CRM_MODEL` (default `claude-haiku-5-5`) and `AI_DAILY_CAP` (default `150` AI messages a day)
   - Then **redeploy** so the secret takes effect.

**How it works**
- **Today:** who to follow up with now, and good first contacts.
- **Leads:** search (spelling is matched loosely), filter, add. Tap a lead for its contacts (call, WhatsApp, email), brochure sending, next step and the full conversation log.
- **Ask AI (💬):** type or speak what happened ("Called Preethi Global, wants 200 kg turmeric, call Thursday"). The AI finds the company and prepares the note; **nothing is saved until Manu taps Save.** He can also ask questions ("who is due today?") and have WhatsApp messages drafted. The AI can never delete data or send messages.
- **Voice:** the 🎤 button uses the phone's built-in speech recognition (English, Malayalam, Hindi, Tamil). It needs internet and microphone permission.
- **More:** import and CSV backups. Export a backup now and then.

**Privacy:** the leads are public business contacts, but still personal data. Keep the password private, and note that what Manu types into the AI box is sent to Anthropic to process.
