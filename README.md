<a id="top"></a>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="Google Account Hardening Guide. Passkeys, recovery, sessions, Gmail, Chrome, Android and privacy in one ordered plan, at three levels: Baseline, Enhanced and Maximum." width="100%">
  </picture>
</p>

<p align="center">
  <a href="#ground-rules"><b>Ground rules</b></a> ·
  <a href="#baseline"><b>Baseline</b></a> ·
  <a href="#if-your-account-is-compromised"><b>Hacked? Start here</b></a> ·
  <a href="#sources"><b>Sources</b></a>
</p>

<p align="center">
  <img alt="Last reviewed October 2026" src="https://img.shields.io/badge/last%20reviewed-October%202026-1a7f37">
  <a href="LICENSE"><img alt="License CC BY-SA 4.0" src="https://img.shields.io/badge/license-CC%20BY--SA%204.0-0969da"></a>
  <a href="CONTRIBUTING.md"><img alt="Corrections welcome" src="https://img.shields.io/badge/corrections-welcome-8250df"></a>
</p>

Your Google account holds your email, files, photos, saved passwords and payment methods. Whoever controls it can reset any account that recovers through your Gmail. Follow the Ground rules, then go as far as your risk requires.

If something no longer matches, [open an issue](https://github.com/iAnonymous3000/google-hardening-guide/issues/new/choose).

## Ground rules

Level: Baseline (free, for everyone).

1. **Google never calls you about your account security. Hang up.** Never give anyone your password, a code, or the web address a page shows after you sign in. Never approve a prompt or create an app password (a passcode that lets an app into your account) because someone asked. Google never emails to verify a caller, has no phone line for sign-in help, and never works with services that offer to recover accounts. It asks for backup codes only at sign-in. A "Google Support" number in an ad or AI summary cannot help you sign in or recover your account.
2. **Never sign in from a link someone sent you, a QR code or an ad.** Type the address or use a bookmark. A passkey, which you unlock with your device's screen lock, works only on Google's real site. Once you have one, distrust a sign-in page that asks for your password and a code instead.
3. **Ignore links and numbers in any email, text, chat or AI summary warning about your security, account deletion, storage or payment.** Check [Recent security activity](https://myaccount.google.com/notifications), your Google account, Google One or the Play Store yourself, since some warnings are real. A real Google sender proves nothing: real calendar invites, Drive shares and `no-reply@google.com` emails have carried attacks. Report phishing instead of only deleting it.
4. **Tap No on any Google prompt ("Trying to sign in?") you did not start**, then check Recent security activity. If someone else tried to sign in, change your password. When an app asks for access to your account, read its name and permissions. Even a real Google screen can give a malicious app access that bypasses your password and 2-Step Verification. If Google says an app is unverified, share nothing unless you trust its developer.
5. **Never run pirated software, fake browser updates, commands a website tells you to paste, or files from sponsorship or job offers.** Fake updates, pasted commands and fake sponsorships spread malware such as infostealers, which steal saved passwords and signed-in sessions.

## Contents

- [Ground rules](#ground-rules)
- [How Google accounts get taken over](#how-google-accounts-get-taken-over)
- [Pick your level](#pick-your-level)
- [Baseline](#baseline)
- [Avoid locking yourself out](#avoid-locking-yourself-out)
- [Enhanced](#enhanced)
- [Maximum](#maximum)
- [If your account is compromised](#if-your-account-is-compromised)
- [Sign-in methods compared](#sign-in-methods-compared)
- [Gmail settings attackers change](#gmail-settings-attackers-change)
- [Your phone number](#your-phone-number)
- [Privacy and AI notes](#privacy-and-ai-notes)
- [Maintenance](#maintenance)
- [Google Workspace accounts](#google-workspace-accounts)
- [Outdated advice to ignore](#outdated-advice-to-ignore)
- [Sources](#sources)
- [About this guide](#about-this-guide)

## How Google accounts get taken over

| Attack | How it works | What reduces it |
|---|---|---|
| **Real-time phishing** | A fake sign-in page relays your password, codes and prompts, then steals your session. Such phishing kits are sold as a service. | [Passkeys](#sign-in-methods-compared), [Advanced Protection](#advanced-protection-program), [rule 2](#ground-rules) |
| **Infostealer malware** | Malware copies browser cookies and saved passwords to reuse your session. | [Rule 5](#ground-rules), [Chrome](#baseline), [signing out](#if-your-account-is-compromised) |
| **SIM swap or port-out** | A criminal moves your number, getting your codes and recovery texts. | [Carrier lock](#your-phone-number), [no text codes](#enhanced) |
| **Consent phishing** | On a real Google screen, you give a malicious app access that can survive password changes. | [Rule 4](#ground-rules), [linked apps](#baseline) |
| **Fake Google support** | A caller asks for a code or prompt approval, sometimes after opening a real support case. | [Rule 1](#ground-rules) |
| **Weak recovery** | Whoever controls your recovery email or phone can reset your account. | [Baseline](#baseline), [Enhanced](#enhanced) |
| **Password reuse** | A password leaked elsewhere is tried on your account. | [A unique password](#baseline), Password Checkup and 2-Step Verification, best with passkeys |
| **Phone theft** | A thief who learned your PIN opens saved passwords. | [Identity Check, Stolen Device Protection](#baseline) |
| **Someone close to you** | Anyone who unlocks your phone can use your account. | [What to check](#if-someone-close-to-you-had-access) |

## Pick your level

| Level | Costs | Suggested for |
|---|---|---|
| **Baseline** | Nothing | Everyone |
| **Enhanced** | Effort, or a purchase such as two security keys | Anyone whose business, income or audience depends on this account, or who manages others' accounts |
| **Maximum** | Convenience | The people Google urges to use [Advanced Protection](#advanced-protection-program) |

Each level adds to the one before, except that Advanced Protection does not allow backup-code downloads, recovery contacts, selfie video or scheduled Takeout exports. The hacked-account and Workspace steps apply at any level. If unsure, do Baseline now and Enhanced next.

<a id="the-20-minute-baseline"></a>

## Baseline

Before removing or replacing any sign-in or recovery method, read [Avoid locking yourself out](#avoid-locking-yourself-out). Signed in to several Google accounts? Check the account picture at the top right of each page.

1. **Run [Security Checkup](https://myaccount.google.com/security-checkup) and fix every warning.** It is Google's review of your sign-in, devices, apps and recovery.
2. **Set a [recovery phone](https://myaccount.google.com/signinoptions/rescuephone) that only you use.** Set a [recovery email](https://myaccount.google.com/recovery/email) you will keep, give it its own 2-Step Verification, and do not make this Gmail its recovery email. Keep Google Voice numbers out of recovery and 2-Step Verification, because Google warns that Google Voice for codes could lock you out. Codes and alerts go to your recovery phone and email, and whoever controls them can reset your account.
3. **Once 2-Step Verification (step 7) is on, print your backup codes.** Find them under [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification) > **Backup codes** and store them with your passport. Getting new codes cancels the old set. Backup codes replace your phone at the second step, not your password.
4. **Add one or two [recovery contacts](https://myaccount.google.com/signinoptions/recoverycontacts): Google users who can respond within 15 minutes.** Ask them to confirm it is you, by voice or in person, before they tap the number you give them. Contacts are usable 7 days after accepting, and not for Advanced Protection, Workspace or child accounts. They vouch for you when other recovery fails, without account access.
5. **Turn on your carrier's [SIM change lock, number transfer lock and account PIN](#your-phone-number).** They stop criminals moving your number to their SIM.
6. **Create a [passkey](https://myaccount.google.com/signinoptions/passkeys) on your phone and each computer you personally own and do not share.** Leave [**Skip password when possible**](https://myaccount.google.com/signinoptions/passwordoptional) on. A fake page cannot use a passkey, but it can still collect your password and codes, which keep working ([why](#sign-in-methods-compared)). Anyone who can unlock that device can sign in as you, even after you sign out.
7. **Turn on [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification), even with passkeys.** Use Google prompts rather than text messages. On iPhone, first install the Gmail or Google app, sign in and allow notifications. Keep any text-message phone until [Enhanced](#enhanced) step 2. Tick **Don't ask again on this device** only on a personal device with a screen lock. Then print your backup codes (step 3). 2-Step Verification stops anyone with only your password, and prompts also help against SIM swaps.
8. **Use a long, random, unique password from a password manager you can open without this account.** Fix every exposed or reused password in [Password Checkup](https://passwords.google.com/checkup/start). Changing your Google password signs you out of most devices. Passwords leaked from other sites get tried on your account.
9. **Sign out [devices](https://myaccount.google.com/device-activity) you no longer own, but not the phone that gets your Google prompts.** If you find a device you do not recognize, follow the [hacked-account steps](#if-your-account-is-compromised), which change your password first. A stolen session needs no password.
10. **Remove unused [linked apps](https://myaccount.google.com/linkedapps) under Access to your Google Account.** Stop unwanted agent use under **Agent access**. Delete [app passwords](https://myaccount.google.com/apppasswords) and reconnect old mail apps with Sign in with Google. Before removing Sign in with Google from a service you still use, set a password there. Old app grants keep reading your data.
11. **On a computer, check Gmail for [forwarding, filters and delegates](#gmail-settings-attackers-change) you did not add.** Attackers add these to keep reading your mail after losing access.
12. **Turn on [Enhanced Safe Browsing](https://myaccount.google.com/account-enhanced-safe-browsing) for your account.** Also turn on **Enhanced protection** at `chrome://settings/security`. The account setting reaches Chrome only if you sign in and sync without a custom passphrase. You get real-time phishing and malware warnings, but Chrome shares more browsing data with Google.
13. **Keep Chrome updated.** At `chrome://extensions`, remove unused extensions and any you do not trust that can "read and change all your data on all websites". Act on Safety Check's extension warnings. On Windows, once your password and second step are at hand, sign out of Google in Chrome and back in. Chrome 146 or later on Windows PCs with a TPM security chip binds new Google sessions to the PC, so stolen ones fail elsewhere.
14. **Android: install updates.** Use a PIN of 6 or more digits. Set a SIM PIN other than your carrier's default, so a thief cannot use your SIM to control your number. Some carriers' default PINs are public. Under **Settings** > **Google** > **All services** > **Theft protection**, turn on **Theft Detection Lock**, **Offline Device Lock** and [**Remote Lock**](https://www.android.com/lock). Turn on **Identity Check** with trusted places; away from them, it needs your fingerprint or face, with no PIN fallback. Install apps only from the Play Store, since apps from outside it may not be vetted. Keep Find Hub, Play Protect and **Scam Detection** in Messages on.
15. **iPhone: install iOS updates.** Turn on [**Stolen Device Protection**](https://support.apple.com/en-us/120340) now. It needs iOS 17.3 or later and must be on before a theft.
16. **In [Calendar settings](https://calendar.google.com/calendar/r/settings), set Event settings > Add invitations to my calendar to Only if the sender is known.** Invites from strangers then arrive only as email.
17. **Set auto-delete to 3 months for Web & App Activity and YouTube History in [Activity controls](https://myactivity.google.com/activitycontrols) and, if you have it, [Search Services History](https://myactivity.google.com/search-services/settings).** 3 months is the shortest option, so the least history is kept.
18. **In [My Activity](https://myactivity.google.com/), turn on Require extra verification under Manage My Activity verification.** It stops someone holding your unlocked device from opening your full history there.
19. **Decide whether Gemini keeps your chats.** In [Gemini Apps Activity](https://myactivity.google.com/product/gemini), turn **Keep Activity** off to stop future chats being reviewed to improve Google services. Or keep it on with auto-delete at 3 months, though reviewed chats outlive auto-delete ([details](#privacy-and-ai-notes)). Use **Temporary Chat** for chats you do not want used to train Google's AI.
20. **Review [Location sharing](https://myaccount.google.com/locationsharing) on each phone you are signed in on, and remove anyone who no longer needs it.** It covers sharing from Maps, Messages, Find Hub, Family Link and Personal Safety. Anyone listed sees where you are.
21. **Set up [Inactive Account Manager](https://myaccount.google.com/inactive) with a wait longer than your longest likely absence.** It alerts or shares data with people you choose if you stop using the account. Sign in to every Google account you keep, including recovery-email accounts, at least every 2 years, because Google may delete personal accounts unused for 2 years. Before you delete an account, move services that use it for recovery or Sign in with Google.

## Avoid locking yourself out

- New passkeys, security keys, 2-Step Verification phones and recovery info can take up to 7 days to take effect. A passkey or security key you already have may speed this up.
- Recovery contacts work only 7 days after they accept, so add them now.
- If you are locked out with 2-Step Verification on, recovery can take 3 to 5 business days, and a few days under Advanced Protection.
- Add the new method, confirm it works at sign-in, have backup codes printed, and only then remove the old one. Make these changes while you still have full access, never while traveling.
- Google recommends setting up more than one sign-in method. Keep them independent, not all on one phone or one sync account: for example a passkey on your phone, a security key and printed backup codes. Under Advanced Protection, use two passkeys or security keys instead of codes.
- When you change numbers, first make the new one your recovery phone, and your 2-Step Verification phone if you use one. Keep the old one working for at least 7 days, because Google may send codes to your previous info for 7 days. Before wiping an old phone, check that prompts reach the new one, your authenticator codes moved, and your recovery phone is current. Turn your carrier lock off before you switch phones, SIMs or carriers, and back on after ([carrier locks](#your-phone-number)).

## Enhanced

1. **Buy two FIDO2 security keys that fit your phone and computer.** Register both as [passkeys](https://myaccount.google.com/signinoptions/passkeys): **Create a passkey** > **Use another device**. Keys added before May 2023 may need removing and re-adding. Carry one and keep one away from home. A key works only on Google's real site.
2. **Check that two security keys or passkeys on different devices work at sign-in and your backup codes are printed.** Then, in [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification), remove text and voice codes and any authenticator app you do not need ([lockout rules](#avoid-locking-yourself-out)). Keep your [**Recovery phone**](https://myaccount.google.com/signinoptions/rescuephone), carrier-locked. If you keep Google Authenticator, do not keep this account's code only in an Authenticator synced to this account. Synced codes go to whoever takes over your account. If you use Authenticator without an account, keep backup codes for every service in it. Phishing kits relay codes, and adding a stronger method removes none of the weaker ones.
3. **Give your [recovery email](https://myaccount.google.com/recovery/email) a passkey or security key.** Use strong sign-in on your Apple Account and password manager too. Google warns that if your Apple Account is taken over, an iCloud backup may let the attacker into your Google account. Your recovery email can reset your account.
4. **If you use Google Password Manager, make sure you know your Google password and have a screen lock.** Then set up **On-device encryption** under [passwords.google.com](https://passwords.google.com/) > **Settings**. Only you can then read your saved passwords, but undoing it deletes them.
5. **Optional: record a [selfie video](https://g.co/signin-selfie) for recovery.** Choose whether Google may use it to improve its systems. It is not for Advanced Protection, Workspace or child accounts. It adds a way back in but gives Google biometric video.
6. **Schedule [Google Takeout](https://takeout.google.com/) every 2 months for a year.** Store archives where this account cannot reach them. Advanced Protection allows no scheduling. A copy of what you select survives losing the account.
7. **Turn off Personalized ads in [My Ad Center](https://myadcenter.google.com/).** It covers partner sites. Turn off shared endorsements in [People & sharing](https://myaccount.google.com/people-and-sharing). Choose **Block third-party cookies** in Chrome, though some sites may break without them. In [Activity controls](https://myactivity.google.com/activitycontrols) > **Web & App Activity**, turn off **Include Chrome history** and **Include voice and audio activity**. Chrome history and voice activity stop going into Web & App Activity, and no name or photo appears beside ads.
8. **Add your phone number, email and address to [Results about you](https://myactivity.google.com/results-about-you).** Request removals, and ask site owners too. It also covers US government ID numbers. Removal hides results from Search, not the page itself. You can get alerts when your details appear in Search.
9. **Disconnect [apps Gemini does not need](https://gemini.google.com/apps).** Delete past chats that used them. Review the [apps AI Mode can use](https://www.google.com/search-personalization), and Gemini in Chrome at `chrome://settings/ai/gemini`, especially tab sharing and letting it browse for you. Connected apps let Gemini use your Gmail, Drive, Photos and YouTube data.
10. **In Drive, set General access to Restricted on anything sensitive.** Only people with access can then open it.

## Maximum

1. **[Enroll](https://landing.google.com/advancedprotection/) in [Advanced Protection](#advanced-protection-program) with two passkeys or security keys, one a security key kept away from home.** One suffices to enroll, but with no backup-code downloads or recovery contacts, losing it means days of recovery ([lockout rules](#avoid-locking-yourself-out)).
2. **Android 16 or later: turn on Android's own [Advanced Protection mode](https://support.google.com/android/answer/16339980).** Using apps from outside the Play Store? Read that page first. The mode blocks unknown apps and, on supported phones, 2G, which can leave you without signal where only 2G is available.
3. **iPhone: turn on [Lockdown Mode](https://support.apple.com/en-us/105120) and add [security keys](https://support.apple.com/en-us/102637) to your Apple Account.** Lockdown Mode is Apple's extreme protection. Google warns that an iCloud backup can hold your Google cookies and passkeys. Apple requires at least two keys and warns that losing all trusted devices and keys could lock you out permanently.
4. **Keep only the Gmail or Drive [linked apps](https://myaccount.google.com/linkedapps) you strictly need.** Each can read or change your mail or files.
5. **Use a separate device, not just a browser profile, for your most important accounts.** Infostealers take cookies from every browser on a device.

### Advanced Protection Program

Google recommends it for anyone at elevated risk of targeted online attacks. That includes journalists, activists, political campaign staffers, business leaders, IT admins, and anyone whose account holds valuable files or sensitive information. It is free, and you can leave.

| Area | What changes |
|---|---|
| Sign-in | Every new device needs a passkey or security key. Weaker methods stop working. |
| Apps | Only Google and verified apps reach sensitive Gmail and Drive data. App passwords stop, and Apps Script asking for mail, documents or photos may be blocked. |
| Android | Apps install only from verified stores. |
| Recovery | Takes a few days. No backup-code downloads, recovery contacts or selfie video. |
| Takeout | Exports wait 2 days; no scheduling. |

1. Register two passkeys or security keys on the [Passkeys](https://myaccount.google.com/signinoptions/passkeys) page.
2. Enroll at [g.co/advancedprotection](https://landing.google.com/advancedprotection/) with a registered key at hand, not while traveling.
3. Where a device or app asks, sign in again with your passkey or security key. Check your apps; Gmail and iPhone Mail work.

<a id="13-if-your-account-is-compromised"></a>

## If your account is compromised

Whatever your level, go in order.

1. **Use a clean device you have signed in on before.** Scan any device that may have malware with trusted antivirus software, or reinstall it, before you sign in on it again. In Chrome, remove extensions you do not recognize. Do not wipe the phone that gets your Google prompts or codes until you are back in. Stolen cookies keep working after the malware is gone, until you sign those sessions out.
2. **Get back in.** If someone moved your number to their SIM, first get it back through your carrier. Until then, your text codes go to them. If you cannot sign in, use [g.co/recover](https://g.co/recover) on a device and in a place where you usually sign in. On a work or school account, contact your admin instead. Start now if someone changed your recovery phone or email: Google may send codes to your previous info for 7 days. Answer every question, guess rather than skip, and retry later from the same device. Recovery contacts and selfie video help only if set up beforehand. Google's [hacked-account guide](https://support.google.com/accounts/answer/6294825) covers edge cases.
3. **Change your password.** In your Google account, go to **Security & sign-in** > [**Password**](https://myaccount.google.com/signinoptions/password). This also revokes app passwords. A password change does not end every session. Then [sign out](https://myaccount.google.com/device-activity) any you do not recognize, and every device that may have had malware. Before signing out the phone that gets your Google prompts, make sure you have another way in.
4. **Check sign-in methods.** Remove [passkeys and security keys](https://myaccount.google.com/signinoptions/passkeys), phones, authenticators and [recovery contacts](https://myaccount.google.com/signinoptions/recoverycontacts) you did not add. Restore your [recovery phone](https://myaccount.google.com/signinoptions/rescuephone) and [email](https://myaccount.google.com/recovery/email). Then turn [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification) back on if it is off. Google may mark methods it thinks an attacker added "at risk" and remove them after 30 days. To keep one you added, select **Re-enable** in Recent security activity; this needs a trusted passkey or security key.
5. **Remove unknown [linked apps](https://myaccount.google.com/linkedapps).** Their access can outlive a password change, and removing them does not delete data they already copied.
6. **Audit Gmail.** Use [this table](#gmail-settings-attackers-change).
7. **Check what was touched.** Review [Recent security activity](https://myaccount.google.com/notifications), [My Activity](https://myactivity.google.com/), Drive and Photos sharing, your YouTube channel, and charges. [Report unknown charges](https://payments.google.com/payments/unauthorizedtransactions).
8. **Contain it.** Change the passwords saved in Google Password Manager and any you reused. Change the passwords of accounts that use this Gmail for recovery, for example your bank, and warn your contacts if the attacker wrote as you.
9. **Upgrade.** Add passkeys or security keys, remove text codes only after the new method has signed you in ([lockout rules](#avoid-locking-yourself-out)), and consider [Advanced Protection](#advanced-protection-program), which removes backup-code downloads and recovery contacts.

### If someone close to you had access

From a device they cannot reach, review signed-in devices, passkeys, recovery info, location sharing, your family group, and Gmail delegates and forwarding. Changes may alert them, so plan your safety first ([Refuge's guide](https://refugetechsafety.org/guides-google-account/), third-party).

## Sign-in methods compared

A fake sign-in page can relay codes and prompts as you enter them, but not a passkey or security key, which works only on Google's real site.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/sign-in-strength-dark.svg">
    <img src="assets/sign-in-strength-light.svg" alt="Sign-in methods by phishing resistance. Passkeys and security keys resist phishing. Below a line marking what a fake sign-in page can relay: Google prompts and authenticator codes are phishable; text or voice codes and a password alone are weak. No method stops malware that steals a signed-in session." width="680">
  </picture>
</p>

Adding a passkey removes none of your other methods, and your password still works. On a personal account outside Advanced Protection, Google can offer them under **Try another way**, so a passkey adds little phishing resistance while weak fallbacks stay on. Only Advanced Protection, or a work or school admin, can make passkeys or security keys mandatory.

A Google prompt shows the device, location and time, but Google only sometimes asks you to match a number, so a relayed sign-in can look normal.

## Gmail settings attackers change

If you find forwarding, a filter or a delegate you did not add, change your password first ([hacked-account steps](#if-your-account-is-compromised)), then remove it. If you use several Google accounts, check the account picture at the top right after each link opens. On a computer, open Gmail, then **Settings** > **See all settings**.

| Tab | What to look for | Link |
|---|---|---|
| Forwarding and POP/IMAP | Forwarding addresses and POP access that you did not add | [Open Forwarding](https://mail.google.com/mail/u/0/#settings/fwdandpop) |
| Filters and Blocked Addresses | Filters that forward, delete, archive or mark mail as read, and blocked senders, that you did not add | |
| Accounts and Import | Delegates under **Grant access to your account**, who can read, send and delete your mail, and **Send mail as** addresses that you did not add | [Open Accounts](https://mail.google.com/mail/u/0/#settings/accounts) |
| General | Vacation responder and signature text that you did not write | |

Personal Gmail no longer lets you turn IMAP off, so control which mail apps read your inbox in [Linked apps](https://myaccount.google.com/linkedapps) and [App passwords](https://myaccount.google.com/apppasswords).

## Your phone number

| US carrier | What to turn on | Where |
|---|---|---|
| T-Mobile | SIM Protection, Port Out Protection and an account PIN | T-Life app security settings. Port Out Protection is a line add-on ([help](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud)) |
| Verizon | SIM Protection and Number Lock | My Verizon > Account settings > Security settings ([help](https://www.verizon.com/support/knowledge-base-309294/)) |
| AT&T | Wireless Account Lock | Only in the AT&T app, on a device active on the account. Postpaid: person icon > Wireless account lock. Prepaid: Profile & Settings > Account Info & Preferences > Wireless Account Lock ([help](https://www.att.com/support/article/wireless/000102016/)) |

Elsewhere, ask your carrier for a SIM change lock, a number transfer lock and an account PIN.

A lock left on can block a switch. T-Mobile returns an error if SIM Protection is on during a SIM or eSIM change. Verizon keeps SIM changes blocked for 15 minutes after you turn it off.

## Privacy and AI notes

- **Gemini** keeps chats for up to 72 hours even with Keep Activity off or in a Temporary Chat. People, including outside service providers, review a sample of chats; those sent to providers are disconnected from your account first. Reviewed chats are kept up to 3 years, even after you delete your activity. Google asks you not to enter anything you would not want a reviewer to see.
- **Search Services History** starts with your Web & App Activity choice. Google says that history, including AI Mode conversations and what AI Mode draws from connected apps, can be used to improve its AI models, with human review.
- **Gmail's smart-feature switches**, under **Settings** > **General**, control whether Gmail and Workspace data feed Gemini and other Google products. Google says it does not train its AI models on your Gmail without permission, but what you share with the Gemini app may be used for training.

## Maintenance

A suggested schedule:

- **Monthly:** [Recent security activity](https://myaccount.google.com/notifications) and [Your devices](https://myaccount.google.com/device-activity).
- **Every 3 months:** [Security Checkup](https://myaccount.google.com/security-checkup), [Password Checkup](https://passwords.google.com/checkup/start), [Linked apps](https://myaccount.google.com/linkedapps) and the [Gmail settings](#gmail-settings-attackers-change).
- **Every 6 months:** sign in once with each security key, confirm your recovery info and contacts, and find your backup codes.
- **Yearly:** privacy controls, Inactive Account Manager, a new Takeout schedule, and a sign-in to each old account.
- **After any alert:** Security Checkup.
- **Changing number or phone:** see [Avoid locking yourself out](#avoid-locking-yourself-out).

## Google Workspace accounts

On a work or school account, your admin controls 2-Step Verification methods, third-party app access, Gmail forwarding and delegation, and account recovery. Ask them about any setting that is missing or grayed out. Ask them to require passkeys or security keys and to restrict high-risk app access. Your admin can block Advanced Protection but cannot force it on you. Recovery contacts and selfie video are not available. Super admins should use a dedicated admin account only for admin tasks and a separate account for daily work.

## Outdated advice to ignore

| Old advice | Today |
|---|---|
| Change passwords every 90 days | NIST, the US standards agency, says no forced periodic changes; change a password when there is evidence of a leak. |
| Any 2-Step Verification stops phishing | Phishing kits relay codes and prompts; only passkeys and security keys resist. |
| 2-Step Verification needs a phone number | Not since May 2024. An authenticator app or security key works. |
| Google's dark web report | Shut down in February 2026. Use Password Checkup and [Have I Been Pwned](https://haveibeenpwned.com/). |
| Location History at google.com/maps/timeline | Timeline is on your device, off by default, in the Maps app. |
| Confidential mode encrypts Gmail | Personal Gmail has no end-to-end encryption, and recipients can screenshot it. Use an end-to-end encrypted messenger for anything sensitive. |
| A VPN protects your account on public Wi-Fi | Google traffic is already encrypted with HTTPS. |
| Delete your recovery phone to stop SIM swaps | Google uses it to get you back in; lock it at your carrier. |
| Set security questions | You can no longer add them. |

## Sources

Every claim traces to a page below. Primary sources come first; third-party research and press are labeled.

<details>
<summary><b>Ground rules and threats</b></summary>

- [Google support call scams](https://support.google.com/faqs/answer/17170932)
- [Google Ads support calls](https://support.google.com/business/answer/6212928)
- [Hacked-account guide](https://support.google.com/accounts/answer/6294825)
- [Report phishing](https://support.google.com/mail/answer/8253)
- [Third-party app access](https://support.google.com/accounts/answer/14012355)
- [Unverified apps](https://support.google.com/accounts/answer/14013600)
- [Fraud and scams advisory, June 2026](https://blog.google/innovation-and-ai/technology/safety-security/fraud-scams-advisory-june-2026/)
- [App password and code lures](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia)
- [Cookie theft aimed at creators](https://blog.google/threat-analysis-group/phishing-campaign-targets-youtube-creators-cookie-theft-malware/)
- [Password reuse and breaches](https://security.googleblog.com/2019/02/protect-your-accounts-from-data.html)
- [When app access ends](https://developers.google.com/identity/protocols/oauth2)
- [Storage over quota](https://support.google.com/googleone/answer/9312312)
- [Declined Play payments](https://support.google.com/googleplay/answer/9818348)
- FBI: [Consent phishing, September 2026](https://www.ic3.gov/PSA/2026/PSA260901)
- FBI: [SIM swapping, February 2022](https://www.ic3.gov/PSA/2022/PSA220208)
- FTC: [Recover a hacked account](https://consumer.ftc.gov/articles/how-recover-your-hacked-email-or-social-media-account)
- Third-party research: [Elastic on Tycoon 2FA](https://www.elastic.co/security-labs/threat-command/tycoon-2fa-aitm-detection-engineering)
- Third-party research: [Brown University IT on Drive shares](https://it.brown.edu/phish-bowl-alerts/google-drive-legitimate-notificationsmalicious-files)
- Third-party research: [0DIN on Gemini summaries](https://0din.ai/blog/phishing-for-gemini)
- Third-party research: [Refuge on securing a Google account](https://refugetechsafety.org/guides-google-account/)
- Press: [BleepingComputer on a real Google email used for phishing](https://www.bleepingcomputer.com/news/security/phishers-abuse-google-oauth-to-spoof-google-in-dkim-replay-attack/)
- Press: [BleepingComputer on Calendar phishing](https://www.bleepingcomputer.com/news/security/ongoing-phishing-attack-abuses-google-calendar-to-bypass-spam-filters/)
- Press: [Gizmodo on fake support numbers](https://gizmodo.com/ai-scam-phone-numbers-2000697589)

</details>

<details>
<summary><b>Sign-in and passwords</b></summary>

- [Passkeys](https://support.google.com/accounts/answer/13548313)
- [2-Step Verification](https://support.google.com/accounts/answer/185839)
- [2-Step Verification problems](https://support.google.com/accounts/answer/185834)
- [Google prompts](https://support.google.com/accounts/answer/7026266)
- [Backup codes](https://support.google.com/accounts/answer/1187538)
- [Security keys](https://support.google.com/accounts/answer/6103523)
- [Google Authenticator](https://support.google.com/accounts/answer/1066447)
- [App passwords](https://support.google.com/accounts/answer/185833)
- [On-device encryption](https://support.google.com/accounts/answer/11350823)
- [Password Checkup](https://support.google.com/accounts/answer/9457609)
- [Security Checkup](https://support.google.com/accounts/answer/46526)
- [At-risk sign-in methods](https://support.google.com/accounts/answer/17137073)
- [World Password Day 2026](https://blog.google/innovation-and-ai/technology/safety-security/world-password-day-2026/)
- [Passkeys and phishing](https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html)
- [Adding 2-Step Verification methods, May 2024](https://workspaceupdates.googleblog.com/2024/05/updates-for-configuring-two-step-verification-for-your-google-account.html)
- NIST: [SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
- CISA: [Phishing-resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)
- CISA: [Mobile communications guidance](https://www.cisa.gov/sites/default/files/2025-12/guidance-mobile-communications-best-practices_508c.pdf)

</details>

<details>
<summary><b>Recovery and lockout</b></summary>

- [Recovery phone and email](https://support.google.com/accounts/answer/183723)
- [Recovery contacts](https://support.google.com/accounts/answer/16590793)
- [Recovery contacts launch](https://blog.google/innovation-and-ai/technology/safety-security/recovery-contacts-verify-google-account/)
- [Selfie video](https://support.google.com/accounts/answer/16675622)
- [Selfie for sign-in](https://blog.google/innovation-and-ai/technology/safety-security/selfie-video-sign-in/)
- [Avoid getting locked out](https://support.google.com/accounts/answer/7684753)
- [Recovery tips](https://support.google.com/accounts/answer/7299973)
- [Recover your account](https://support.google.com/accounts/answer/7682439)
- [Inactive Account Manager](https://support.google.com/accounts/answer/3036546)
- [Inactive account policy](https://support.google.com/accounts/answer/12418290)
- [Google Takeout](https://support.google.com/accounts/answer/3024190)

</details>

<details>
<summary><b>Devices, apps and Chrome</b></summary>

- [Your devices](https://support.google.com/accounts/answer/3067630)
- [Password changes and sessions](https://support.google.com/accounts/answer/41078)
- [Linked apps](https://support.google.com/accounts/answer/13533235)
- [Removing app access](https://support.google.com/accounts/answer/16670080)
- [Enhanced Safe Browsing for your account](https://support.google.com/accounts/answer/11577602)
- [Chrome Safe Browsing](https://support.google.com/chrome/answer/9890866)
- [Update Chrome](https://support.google.com/chrome/answer/95414)
- [Chrome Safety Check](https://support.google.com/chrome/answer/10468685)
- [Extension permissions](https://support.google.com/chrome_webstore/answer/186213)
- [Extension permission warnings](https://developer.chrome.com/docs/extensions/reference/permissions-list)
- [Extension Safety Hub](https://developer.chrome.com/blog/extension-safety-hub)
- [Chrome cookies](https://support.google.com/chrome/answer/95647)
- [Gemini in Chrome](https://support.google.com/chrome/answer/16283624)
- [Device-bound sessions](https://blog.google/security/protecting-cookies-with-device-bound-session-credentials/)
- [Device-bound sessions on Windows](https://workspaceupdates.googleblog.com/2026/05/prevent-account-takeovers-with-DBSC-now-generally-available-in-the-Chrome-browser-for-Windows.html)
- [Session binding requirements](https://knowledge.workspace.google.com/admin/security/prevent-cookie-theft-with-session-binding)
- [Fighting cookie theft](https://blog.google/chromium/fighting-cookie-theft-using-device/)

</details>

<details>
<summary><b>Gmail, Calendar and Drive</b></summary>

- [Forwarding](https://support.google.com/mail/answer/10957)
- [Filters](https://support.google.com/mail/answer/6579)
- [Filter actions](https://developers.google.com/workspace/gmail/api/guides/filter_settings)
- [Delegates](https://support.google.com/mail/answer/138350)
- [Send mail as](https://support.google.com/mail/answer/22370)
- [Vacation responder](https://support.google.com/mail/answer/25922)
- [IMAP and POP](https://support.google.com/mail/answer/7126229)
- [Confidential mode](https://support.google.com/mail/answer/7674059)
- [Gmail encryption](https://support.google.com/mail/answer/13317990)
- [Smart features](https://support.google.com/mail/answer/15604322)
- [Gemini in Workspace and your data](https://support.google.com/mail/answer/14615114)
- [Calendar invitations](https://support.google.com/calendar/answer/13159188)
- [Drive sharing](https://support.google.com/drive/answer/2494822)

</details>

<details>
<summary><b>Phones and Advanced Protection</b></summary>

- [Android theft protection](https://support.google.com/android/answer/15146908)
- [Android updates](https://support.google.com/android/answer/7680439)
- [Play Protect](https://support.google.com/googleplay/answer/2812853)
- [Scam Detection](https://blog.google/security/new-ai-powered-scam-detection-features/)
- [Identity Check](https://blog.google/security/android-theft-protection-identity-check-expanded-features/)
- [Android Advanced Protection](https://support.google.com/android/answer/16339980)
- [Android Advanced Protection updates](https://blog.google/security/android-advanced-protection-updates/)
- [Advanced Protection Program](https://support.google.com/accounts/answer/7519408)
- [Advanced Protection questions](https://support.google.com/accounts/answer/7539956)
- [Passkeys in Advanced Protection](https://blog.google/innovation-and-ai/technology/safety-security/google-passkeys-advanced-protection-program/)
- Apple: [iPhone updates](https://support.apple.com/en-us/118575)
- Apple: [Stolen Device Protection](https://support.apple.com/en-us/120340)
- Apple: [Lockdown Mode](https://support.apple.com/en-us/105120)
- Apple: [Security keys](https://support.apple.com/en-us/102637)
- T-Mobile: [Account protection](https://www.t-mobile.com/support/plans-features/help-with-t-mobile-account-fraud)
- Verizon: [SIM Protection and Number Lock](https://www.verizon.com/support/knowledge-base-309294/)
- AT&T: [Wireless Account Lock](https://www.att.com/support/article/wireless/000102016/)

</details>

<details>
<summary><b>Privacy and AI</b></summary>

- [Web & App Activity](https://support.google.com/websearch/answer/54068)
- [Auto-delete](https://support.google.com/accounts/answer/9784401)
- [YouTube history](https://support.google.com/youtube/answer/95725)
- [My Activity verification](https://support.google.com/accounts/answer/7028918)
- [Search Services History](https://support.google.com/websearch/answer/17025248)
- [Manage Search Services History](https://support.google.com/websearch/answer/17024959)
- [AI Mode connected apps](https://support.google.com/websearch/answer/16859283)
- [Gemini privacy hub](https://support.google.com/gemini/answer/13594961)
- [Gemini connected apps](https://support.google.com/gemini/answer/16598406)
- [Gemini Temporary Chat](https://support.google.com/gemini/answer/13275745)
- [Personalized ads](https://support.google.com/My-Ad-Center-Help/answer/12155656)
- [Shared endorsements](https://support.google.com/accounts/answer/3403513)
- [Results about you](https://support.google.com/websearch/answer/12719076)
- [Results about you for ID numbers](https://blog.google/products-and-platforms/products/search/results-about-you-government-id-numbers/)
- [Location sharing](https://support.google.com/accounts/answer/9363497)

</details>

<details>
<summary><b>Workspace and outdated advice</b></summary>

- [Deploy 2-Step Verification](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification)
- [Advanced Protection enrollment](https://knowledge.workspace.google.com/admin/security/enable-user-enrollment-in-the-advanced-protection-program)
- [Control app access](https://knowledge.workspace.google.com/admin/apps/control-which-apps-access-google-workspace-data)
- [Forwarding controls](https://knowledge.workspace.google.com/admin/gmail/let-users-automatically-forward-their-own-gmail-emails)
- [Delegation controls](https://knowledge.workspace.google.com/admin/gmail/let-users-delegate-access-to-a-gmail-account)
- [Password recovery for users](https://knowledge.workspace.google.com/admin/users/set-up-password-recovery-for-users)
- [Super admin accounts](https://knowledge.workspace.google.com/admin/users/security-best-practices-for-administrator-accounts)
- [Dark web report ends](https://support.google.com/websearch/answer/16767242)
- [Timeline on your device](https://support.google.com/accounts/answer/14200149)
- [Timeline in Maps](https://support.google.com/maps/answer/6258979)
- [Location History becomes Timeline](https://blog.google/products-and-platforms/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/)
- Chromium source: [HTTPS preload list](https://github.com/chromium/chromium/blob/main/net/http/transport_security_state_static.json)

</details>

## About this guide

To report a change, [open an issue](https://github.com/iAnonymous3000/google-hardening-guide/issues/new/choose) with a source. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [changelog](CHANGELOG.md).

Licensed [CC BY-SA 4.0](LICENSE). This guide is independent and not affiliated with or endorsed by Google. Settings change, so confirm details on Google's own pages before you rely on them.

<p align="center"><sub>Maintained by <a href="https://profincognito.me">Professor Incognito</a> (<a href="https://x.com/iAnonymous3000">@iAnonymous3000</a>). <a href="#top">Back to top</a></sub></p>
