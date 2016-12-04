def classify_post (row):
   status = row['content'].lower()
   if (('donald' in status) or ('trump' in status)) and (('hillary' in status) or ('clinton' in status)) :
      return 'other'
   elif ('donald' in status) or ('trump' in status) :
      return 'trump'
   elif ('hillary' in status) or ('clinton' in status) :
      return 'clinton'
   else:
      return 'other'

cbs_df['candidate_label'] = cbs_df.apply (lambda row: classify_post (row),axis=1)
cbs_df.head()
