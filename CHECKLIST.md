# Google Account Hardening Checklist

The printable companion to the [full guide](README.md#top). Work top to bottom and tick items as you go. Each level includes the one before it. The guide explains the why behind every line.

**Last reviewed: October 2026.**

## Level 1: Baseline

Everyone. About 20 minutes, no purchases needed.

### Sign-in

- [ ] Run [Security Checkup](https://myaccount.google.com/security-checkup) and fix every warning
- [ ] Create a passkey on your phone and on each computer you use: [Passkeys](https://myaccount.google.com/signinoptions/passkeys)
- [ ] Leave **Skip password when possible** on: [setting](https://myaccount.google.com/signinoptions/passwordoptional)
- [ ] Turn on [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification)
- [ ] Use Google prompts, and read every prompt before you tap it
- [ ] Save your [backup codes](https://myaccount.google.com/two-step-verification/backup-codes) offline
- [ ] Use a long, random password that you use nowhere else
- [ ] Fix every exposed or reused password in [Password Checkup](https://passwords.google.com/checkup/start)

### Recovery

- [ ] Confirm your [recovery email](https://myaccount.google.com/recovery/email): a different address from your Gmail, with its own strong sign-in
- [ ] Confirm your [recovery phone](https://myaccount.google.com/signinoptions/rescuephone): a number only you use, never Google Voice
- [ ] Add one or two [recovery contacts](https://myaccount.google.com/signinoptions/recoverycontacts)

### Access

- [ ] Sign out of devices you do not recognize in [Your devices](https://myaccount.google.com/device-activity)
- [ ] Remove apps you no longer use in [Linked apps](https://myaccount.google.com/linkedapps)
- [ ] Delete [app passwords](https://myaccount.google.com/apppasswords) you do not need
- [ ] Check Gmail [forwarding](https://mail.google.com/mail/u/0/#settings/fwdandpop), [filters](https://mail.google.com/mail/u/0/#settings/filters) and [delegates](https://mail.google.com/mail/u/0/#settings/accounts)

### Browser and phone

- [ ] Turn on [Enhanced Safe Browsing for your account](https://myaccount.google.com/account-enhanced-safe-browsing), and **Enhanced protection** in Chrome
- [ ] Remove Chrome extensions you do not use
- [ ] Keep your phone updated and use a strong screen lock
- [ ] Android: turn on Theft protection and Identity Check, and keep Find Hub and Play Protect on
- [ ] iPhone: turn on Stolen Device Protection, and allow Gmail or Google app notifications for prompts
- [ ] Turn on your carrier's SIM change lock, number transfer lock and account PIN

### Privacy and scams

- [ ] Set auto-delete to 3 months in [Activity controls](https://myactivity.google.com/activitycontrols)
- [ ] Turn on **Require extra verification** in [My Activity](https://myactivity.google.com/)
- [ ] Decide whether Gemini keeps your chats: [Gemini activity](https://myactivity.google.com/product/gemini)
- [ ] In [Calendar settings](https://calendar.google.com/calendar/r/settings), set **Add invitations to my calendar** to known senders or to when you respond
- [ ] Set up [Inactive Account Manager](https://myaccount.google.com/inactive)
- [ ] Remember: Google never calls you about your account security

## Level 2: Enhanced

Money, crypto, a business, an audience or admin access. About an hour plus two security keys.

- [ ] Buy two FIDO2 security keys and register both on the [Passkeys and security keys](https://myaccount.google.com/signinoptions/passkeys) page
- [ ] Remove the phone number from your 2-Step Verification methods
- [ ] Remove authenticator apps you do not need, or use Google Authenticator without an account
- [ ] Protect your recovery email with passkeys or security keys
- [ ] Set up **On-device encryption** in [Google Password Manager](https://passwords.google.com/) settings
- [ ] Gmail: set **Images** to **Ask before displaying external images**
- [ ] Chrome: confirm **Always use secure connections**, block third-party cookies, review Gemini in Chrome
- [ ] Android: turn on Scam Detection, and keep sensitive apps in a Private space
- [ ] Turn off the Chrome history and voice options in Web & App Activity, and check [Search Services History](https://myactivity.google.com/search-services/settings)
- [ ] Turn off personalized ads in [My Ad Center](https://myadcenter.google.com/) and check [partner ads](https://adssettings.google.com/partnerads)
- [ ] Turn off shared endorsements in [People and sharing](https://myaccount.google.com/people-and-sharing)
- [ ] Disconnect apps Gemini does not need: [Connected apps](https://gemini.google.com/apps)
- [ ] Add your contact details to [Results about you](https://myactivity.google.com/results-about-you)
- [ ] Schedule [Google Takeout](https://takeout.google.com/) exports and store them encrypted
- [ ] [Delete services](https://myaccount.google.com/deleteservices) and old accounts you no longer use

## Level 3: Maximum

Journalists, activists, executives, officials, anyone targeted.

- [ ] Enroll in the [Advanced Protection Program](https://landing.google.com/advancedprotection/) with at least two passkeys or security keys
- [ ] Android 16 or later: turn on Advanced Protection device mode
- [ ] iPhone: turn on Lockdown Mode, and add security keys to your Apple Account
- [ ] Remove every linked app with Gmail or Drive access that you do not strictly need
- [ ] Use separate Google accounts for separate roles
- [ ] Do admin work from a dedicated, updated device or browser profile
- [ ] Store a backup security key off-site

## Maintenance

- [ ] Monthly: [Recent security activity](https://myaccount.google.com/notifications) and [Your devices](https://myaccount.google.com/device-activity)
- [ ] Every 3 months: Security Checkup, Password Checkup, Linked apps and Gmail settings
- [ ] Every 6 months: test your backup key, confirm recovery info, locate your backup codes
- [ ] Every year: review privacy controls and Inactive Account Manager, and read the [changelog](CHANGELOG.md)

<sub>Part of the [Google Account Hardening Guide](README.md#top). CC BY-SA 4.0.</sub>
