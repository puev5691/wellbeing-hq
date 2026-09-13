from __future__ import annotations
import html

def between(text,start,end):
    p=text.find(start)
    if p<0:return ''
    p+=len(start); q=text.find(end,p)
    return text[p:] if q<0 else text[p:q]

def article(text,fid):
    p=text.find(f"<article data-fixture='{fid}'")
    if p<0:return ''
    q=text.find('</article>',p)
    return text[p:] if q<0 else text[p:q+10]

def section(text,bucket):
    p=text.find(f"<section data-bucket='{bucket}'")
    if p<0:return ''
    q=text.find('</section>',p)
    return text[p:] if q<0 else text[p:q+10]

def evaluate(name,f,text):
    m=f['metadata']; fid=m['id']; card=article(text,fid)
    nav=between(text,'<h1>Public-safe navigation</h1><ul>','</ul>')
    cur=section(text,'current-public-ready'); research=section(text,'research-candidate')
    hist=section(text,'historical-superseded'); withdrawn=section(text,'withdrawn-historical')
    c={
      'absent_from_public_navigation':(fid not in nav,'fixture id present in public navigation'),
      'blocked_placeholder_only':('CONTENT SUPPRESSED — BLOCKED / QUARANTINE' in card and html.escape(f['safe_body']) not in card,'blocked card did not contain only suppression placeholder'),
      'blocking_reason_class_visible':(bool(m['expected_blocking_reason']) and html.escape(m['expected_blocking_reason']) in card,'blocking reason class not visible'),
      'blocked_body_absent':('blocked_body' not in text and html.escape(f['safe_body']) not in card,'blocked body/safe body leaked'),
      'no_canonical_public_url':(m['canonical_public_url'] is None and 'canonical_public_url' not in card,'canonical public URL present'),
      'absent_from_current_bucket':(fid not in cur,'fixture present in current bucket'),
      'candidate_badge_persistent':('CANDIDATE / NOT CURRENT' in card,'candidate badge missing'),
      'no_public_ready_claim':('PUBLIC-READY' not in card,'public-ready claim present'),
      'release_unassessed_visible':('release_unassessed' in card,'release_unassessed missing'),
      'reviewer_private_note_absent':('reviewer_private_note' not in text,'reviewer_private_note leaked'),
      'current_bucket_only':(fid in cur and fid not in research and fid not in hist and fid not in withdrawn,'fixture not confined to current bucket'),
      'public_ready_badge_visible':('PUBLIC-READY / SYNTHETIC' in card,'public-ready badge missing'),
      'provenance_visible':(m['provenance_locator'] in card and m['immutable_identity']['id'] in card,'safe provenance/immutable identity missing'),
      'derivative_parent_visible':(bool(m['derivative_of']) and m['derivative_of'] in card and m['derivative_type'] in card,'derivative parent/type missing'),
      'safe_body_visible':(html.escape(f['safe_body']) in card,'safe body missing'),
      'internal_test_note_absent':('internal_test_note' not in text,'internal_test_note leaked'),
      'secret_block_badge_visible':('SECRET-LIKE / BLOCKED' in card,'secret-like block badge missing'),
      'secret_like_value_absent':('secret_like_value' not in text and 'SYNTHETIC_SECRET_VALUE_DO_NOT_RENDER_7KQ9' not in text,'secret-like value leaked'),
      'raw_detection_sample_absent':('raw_detection_sample' not in text,'raw detection sample leaked'),
      'SIS_review_required_visible':('SIS REVIEW REQUIRED' in card,'SIS review warning missing'),
      'superseded_badge_visible':('<b>SUPERSEDED</b>' in card,'superseded badge missing'),
      'successor_locator_visible':(bool(m['superseded_by']) and all(x in card for x in m['superseded_by']),'successor locator missing'),
      'historical_bucket_only':(fid in hist and fid not in cur and fid not in research and fid not in withdrawn,'fixture not confined to historical bucket'),
      'stale_warning_visible':('STALE — superseded by newer version' in card,'stale warning missing'),
      'withdrawn_badge_visible':('<b>WITHDRAWN</b>' in card,'withdrawn badge missing'),
      'withdrawal_record_visible':('WITHDRAWAL RECORD — prior body is not presented as current' in card,'withdrawal record missing'),
      'prior_body_not_presented_as_current':(html.escape(f['safe_body']) not in cur and fid not in cur,'withdrawn prior body/current placement observed'),
      'release_withdrawn_visible':('release_withdrawn' in card,'release_withdrawn missing')}
    return c.get(name,(False,'unknown assertion name'))
