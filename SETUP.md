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
- **Manu's enquiry desk:** `https://josons.pages.dev/admin.html`
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
