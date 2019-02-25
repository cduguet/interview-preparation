# Maps and Hashing

## Sets
Sets are like lists except:  
- Sets cannot have repeated elements  
- Sets don't have order

> A Map is a Set of keys 
### Map : <Key, Value>

## Hashing 
Is used to order elements of very large sets much easier
But sometimes hashing can have collisions.

Solutions: 
 - Instead of an simple array of hashe, we can use a Bucket (array inside the ordered element). Then we put the collided elements in the same bucket. But we lose efficiency in th ecomplexity of search: 
 O(1) -> O(n)

 - Improve the Hash function. Thisis might be costly to migrate

 - Hash of hashes. 
 
 > Load factor: No. of Entries / No. buckets in total

 ## Hash Maps
 a Hash table of a map 
`Key`  ----------> `Hash`    
`<Key, Value >` -> `Value`  

<Key, Value> = ` {"Paul": phone#}`  
Hash(`Paul`) -> `index`  
Store `<Paul, phone#>` in `array[index]`

### Hashing of String keys
ASCII of string s="cristian":  
` s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1] `





