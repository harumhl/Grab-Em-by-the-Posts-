def classify_post (row):
   status = row['status_message'].lower()
   if (('donald' in status) or ('trump' in status)) and (('hillary' in status) or ('clinton' in status)) :
      return 'other'
   if ('donald' in status) or ('trump' in status) :
      return 'trump'
   if ('hillary' in status) or ('clinton' in status) :
      return 'clinton'
   return 'other'

cbs_df['candidate_label'] = cbs_df.apply (lambda row: classify_post (row),axis=1)
cbs_df.head()
