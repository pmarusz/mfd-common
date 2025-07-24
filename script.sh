commit_message=$(git log -1 --pretty=%B)

# Define the regex pattern
pattern='^(feat|fix|docs|test|ci|refactor|perf|chore|revert):\s+.+\n\nSigned-off-by:\s+.+'

# Check the last commit message against the pattern
if ! [[ "$commit_message" =~ $pattern ]]; then
    echo "Last commit message does not match the required pattern:"
    echo "$commit_message"
    exit 1
fi